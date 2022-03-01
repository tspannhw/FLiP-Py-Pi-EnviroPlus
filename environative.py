from time import sleep
from math import isnan
import time
import sys
import datetime
import subprocess
import sys
import os
from subprocess import PIPE, Popen
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import psutil
import base64
import uuid
import socket 
from smbus2 import SMBus
from bme280 import BME280
import time
import logging
#import paho.mqtt.client as mqtt
#from kafka import KafkaProducer
#from kafka.errors import KafkaError
import pulsar
from pulsar.schema import *

### Schema Object
# https://pulsar.apache.org/docs/en/client-libraries-python/
# https://pulsar.apache.org/api/python/

class enviroplus(Record):
    adjtemp = String()
    adjtempf = String()
    amplitude100 = Float()
    amplitude1000 = Float()
    amplitude500 = Float()
    amps = Float()
    cpu = Float()
    cputemp = String()
    cputempf = String()
    diskusage = String()
    endtime = String()
    gasko = String()
    highnoise = Float()
    host = String()
    hostname = String()
    humidity = Float()
    ipaddress = String()
    lownoise = Float()
    lux = Float()
    macaddress = String()
    memory = Float()
    midnoise = Float()
    nh3 = Float()
    oxidising = Float()
    pressure = Float()
    proximity = Integer()
    reducing = Float()
    rowid = String()
    runtime = Integer()
    starttime = String()
    systemtime = String()
    temperature = String()
    temperaturef = String()
    ts = Integer()
    uuid = String()

from enviroplus.noise import Noise
noise = Noise()

currenttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
starttime = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
start = time.time()

try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559
from enviroplus import gas
import ST7735
from PIL import Image, ImageDraw, ImageFont
disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

i = 0

external_IP_and_port = ('198.41.0.4', 53)  # a.root-servers.net
socket_family = socket.AF_INET

def IP_address():
        try:
            s = socket.socket(socket_family, socket.SOCK_DGRAM)
            s.connect(external_IP_and_port)
            answer = s.getsockname()
            s.close()
            return answer[0] if answer else None
        except socket.error:
            return None

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address
# Random Word
def randomword(length):
 return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()) for i in range(length))

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])


# Timer
start = time.time()
packet_size=3000

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ipaddress = IP_address()

# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.25

client = pulsar.Client('pulsar://pulsar1:6650')
producer = client.create_producer(topic='persistent://public/default/rp4enviroplus' ,schema=JsonSchema(enviroplus),properties={"producer-name": "enviroplus-py-sensor","producer-id": "enviroplus-sensor" })

try:
    while (1):
        enviroRec = enviroplus()
        # Create unique id
        uniqueid = 'rpi4_uuid_{0}_{1}'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))
        uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
        cpu_temps = [get_cpu_temperature()] * 5
        cpu_temp = round(get_cpu_temperature(),1)
        cputempf = str(round(9.0/5.0 * float(cpu_temp) + 32))

        # Smooth out with some averaging to decrease jitter
        cpu_temps = cpu_temps[1:] + [cpu_temp]
        avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
        raw_temp = bme280.get_temperature()
        adjtemp = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
        adjtemp = round(adjtemp,1)
        bme280temp = round(bme280.get_temperature(),1)
        adjtempf = (adjtemp * 1.8) + 12
        adjtempf = round(adjtempf,1)
        temperaturef = (bme280temp*1.8)+12
        temperaturef = round(temperaturef,1)
        amps = noise.get_amplitudes_at_frequency_ranges([
            (100, 200),
            (500, 600),
            (1000, 1200)
        ])

        low, mid, high, amp = noise.get_noise_profile()
        end = time.time()
        usage = psutil.disk_usage("/")
        readings = gas.read_all()

        enviroRec.adjtemp = str(adjtemp)
        enviroRec.adjtempf = str(adjtempf)
        enviroRec.amplitude100 = float(round(amps[0],1))
        enviroRec.amplitude1000 = float(round(amps[2],1))
        enviroRec.amplitude500 = float(round(amps[1],1))
        enviroRec.amps = float(round(amp,1))
        enviroRec.cpu = float(psutil.cpu_percent(interval=1))
        enviroRec.cputemp = str(cpu_temp)
        enviroRec.cputempf = str(cputempf)
        enviroRec.diskusage = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
        enviroRec.endtime = '{0}'.format( str(end ))
        enviroRec.gasko = str(readings)
        enviroRec.highnoise = float(round(high,1))
        enviroRec.host = os.uname()[1]
        enviroRec.hostname = host_name
        enviroRec.humidity = float(round(bme280.get_humidity(),1))
        enviroRec.ipaddress = ipaddress
        enviroRec.lownoise = float(round(low,1))
        enviroRec.lux = float(round(ltr559.get_lux(),1))
        enviroRec.macaddress = psutil_iface('wlan0')
        enviroRec.memory = float(psutil.virtual_memory().percent)
        enviroRec.midnoise = float(round(mid,1))
        enviroRec.nh3 = float(round(readings.nh3 / 1000,1))
        enviroRec.oxidising = float(round(readings.oxidising / 1000,1))
        enviroRec.pressure =  float(round(bme280.get_pressure(),1))
        enviroRec.proximity = int(round(ltr559.get_proximity(),1))
        enviroRec.reducing  = float(round(readings.reducing / 1000,1))
        enviroRec.runtime =  int(round(end - start)) 
        enviroRec.starttime = str(starttime)
        enviroRec.systemtime = str(datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
        enviroRec.temperature = str(bme280temp)
        enviroRec.temperaturef = str(temperaturef)
        enviroRec.ts =  int( time.time() )
        enviroRec.rowid =  str(uuid2)
        enviroRec.uuid = str(uniqueid)

        fa=open("/opt/demo/logs/envprec.log", "a+")
        fa.write(str(enviroRec) + "\n")
        fa.close()

        print(enviroRec)

        producer.send(enviroRec,partition_key=str(uniqueid))

except KeyboardInterrupt:
    pass

client.close()
