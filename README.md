# FLiP-Py-Pi-EnviroPlus
FLiP-Py-Pi-EnviroPlus.  Apache Flink, Apache Pulsar, Apache Spark, Python, Raspberry Pi, Enviro+ sensors.   Tim streamnative

### Code

### Json Schema

````
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

````

### Example Data

````
{'adjtemp': '26.7', 'adjtempf': '60.1', 'amplitude100': 1.0, 'amplitude1000': 0.2, 'amplitude500': 0.3, 'amps': 0.3, 'cpu': 0.0, 'cputemp': '45.7', 'cputempf': '114', 'diskusage': '31435.2 MB', 'endtime': '1646156801.2777877', 'gasko': 'Oxidising: 10165.41 Ohms\nReducing: 87589.74 Ohms\nNH3: 15213.87 Ohms', 'highnoise': 0.1, 'host': 'rp4', 'hostname': 'rp4', 'humidity': 16.4, 'ipaddress': '192.168.1.209', 'lownoise': 0.5, 'lux': 55.9, 'macaddress': 'a2:3f:eb:35:a7:99', 'memory': 7.2, 'midnoise': 0.2, 'nh3': 15.2, 'oxidising': 10.2, 'pressure': 1015.5, 'proximity': 0, 'reducing': 87.6, 'rowid': '20220301174640_34f06310-caa3-4e96-9766-6e8da40ad516', 'runtime': 6, 'starttime': '03/01/2022 12:46:34', 'systemtime': '03/01/2022 12:46:42', 'temperature': '32.7', 'temperaturef': '70.9', 'ts': 1646156802, 'uuid': 'rpi4_uuid_shx_20220301174640'}

````

### Topic

persistent://public/default/rp4enviroplus

### Run

````
bin/pulsar-admin topics create persistent://public/default/rp4enviroplus

bin/pulsar-client consume "persistent://public/default/rp4enviroplus" -s "rp4enviroplusrdr" -n 0

----- got message -----
key:[rpi4_uuid_upn_20220301174920], properties:[], content:{
 "adjtemp": "26.8",
 "adjtempf": "60.2",
 "amplitude100": 1.0,
 "amplitude1000": 0.2,
 "amplitude500": 0.3,
 "amps": 0.3,
 "cpu": 0.0,
 "cputemp": "45.2",
 "cputempf": "113",
 "diskusage": "31435.2 MB",
 "endtime": "1646156961.7520766",
 "gasko": "Oxidising: 11618.00 Ohms\nReducing: 95351.35 Ohms\nNH3: 17596.18 Ohms",
 "highnoise": 0.0,
 "host": "rp4",
 "hostname": "rp4",
 "humidity": 16.3,
 "ipaddress": "192.168.1.209",
 "lownoise": 0.4,
 "lux": 55.9,
 "macaddress": "a2:3f:eb:35:a7:99",
 "memory": 7.2,
 "midnoise": 0.1,
 "nh3": 17.6,
 "oxidising": 11.6,
 "pressure": 1015.5,
 "proximity": 0,
 "reducing": 95.4,
 "rowid": "20220301174920_13b9c774-c221-4ebc-8e17-cb2054954f14",
 "runtime": 6,
 "starttime": "03/01/2022 12:49:15",
 "systemtime": "03/01/2022 12:49:22",
 "temperature": "32.7",
 "temperaturef": "70.9",
 "ts": 1646156962,
 "uuid": "rpi4_uuid_upn_20220301174920"
}

 
````

### References

* https://shop.pimoroni.com/products/enviro?variant=31155658457171
* https://www.datainmotion.dev/2019/12/iot-series-minifi-agent-on-raspberry-pi.html
* https://github.com/tspannhw/meetup-sensors
* https://github.com/tspannhw/minifi-enviroplus
