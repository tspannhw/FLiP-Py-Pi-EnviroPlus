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

### Flink SQL

````
CREATE CATALOG pulsar WITH (
   'type' = 'pulsar',
   'service-url' = 'pulsar://pulsar1:6650',
   'admin-url' = 'http://pulsar1:8080',
   'format' = 'json'
);

USE CATALOG pulsar;

SHOW TABLES;

    ______ _ _       _       _____  ____  _         _____ _ _            _  BETA   
   |  ____| (_)     | |     / ____|/ __ \| |       / ____| (_)          | |  
   | |__  | |_ _ __ | | __ | (___ | |  | | |      | |    | |_  ___ _ __ | |_ 
   |  __| | | | '_ \| |/ /  \___ \| |  | | |      | |    | | |/ _ \ '_ \| __|
   | |    | | | | | |   <   ____) | |__| | |____  | |____| | |  __/ | | | |_ 
   |_|    |_|_|_| |_|_|\_\ |_____/ \___\_\______|  \_____|_|_|\___|_| |_|\__|
          
        Welcome! Enter 'HELP;' to list all available commands. 'QUIT;' to exit.


Flink SQL> CREATE CATALOG pulsar WITH (
>    'type' = 'pulsar',
>    'service-url' = 'pulsar://pulsar1:6650',
>    'admin-url' = 'http://pulsar1:8080',
>    'format' = 'json'
> );
[INFO] Execute statement succeed.

Flink SQL> USE CATALOG pulsar;
[INFO] Execute statement succeed.

Flink SQL> show tables;
+---------------------------+
|                table name |
+---------------------------+
| ble-tempE0:17:54:C1:D8:4C |
|                  breakout |
|                      chat |
|                     chat2 |
|                 chatfiles |
|                  chatlog2 |
|                chatresult |
|               chatresult2 |
|                    crypto |
|            custom-routing |
|           delayed-message |
|                dotnettest |
|           dynamic-topic-0 |
|           dynamic-topic-1 |
|           dynamic-topic-2 |
|           dynamic-topic-3 |
|           dynamic-topic-4 |
|                    energy |
|             energy-influx |
|                 energylog |
|                 ex1-basic |
|                 flaky-DLQ |
|        funhouselightstate |
|             funhousestate |
|                hfptransit |
|               input-topic |
|                      iot3 |
|                iotelastic |
|             iotjetsonjson |
|            iotjetsonjson2 |
|              jetsoninflux |
|                   moptest |
|                    mqtt-2 |
|              nodejs-topic |
|             nvidia-sensor |
|                pi-thermal |
|           pi-thermal-avro |
|                pi-weather |
|           pi-weather-avro |
|                     rp400 |
|             rp4enviroplus |
|           scyllacdcsource |
|                   seeking |
|                   sensors |
|                    stocks |
|                   stocks2 |
|   telegraf%2Fhost01%2Fcpu |
|               telegrafcpu |
|               telegrafmem |
|                  transcom |
|                   weather |
+---------------------------+
51 rows in set

Flink SQL> describe rp4enviroplus;
+---------------+--------+------+-----+--------+-----------+
|          name |   type | null | key | extras | watermark |
+---------------+--------+------+-----+--------+-----------+
|       adjtemp | STRING | true |     |        |           |
|      adjtempf | STRING | true |     |        |           |
|  amplitude100 |  FLOAT | true |     |        |           |
| amplitude1000 |  FLOAT | true |     |        |           |
|  amplitude500 |  FLOAT | true |     |        |           |
|          amps |  FLOAT | true |     |        |           |
|           cpu |  FLOAT | true |     |        |           |
|       cputemp | STRING | true |     |        |           |
|      cputempf | STRING | true |     |        |           |
|     diskusage | STRING | true |     |        |           |
|       endtime | STRING | true |     |        |           |
|         gasko | STRING | true |     |        |           |
|     highnoise |  FLOAT | true |     |        |           |
|          host | STRING | true |     |        |           |
|      hostname | STRING | true |     |        |           |
|      humidity |  FLOAT | true |     |        |           |
|     ipaddress | STRING | true |     |        |           |
|      lownoise |  FLOAT | true |     |        |           |
|           lux |  FLOAT | true |     |        |           |
|    macaddress | STRING | true |     |        |           |
|        memory |  FLOAT | true |     |        |           |
|      midnoise |  FLOAT | true |     |        |           |
|           nh3 |  FLOAT | true |     |        |           |
|     oxidising |  FLOAT | true |     |        |           |
|      pressure |  FLOAT | true |     |        |           |
|     proximity |    INT | true |     |        |           |
|      reducing |  FLOAT | true |     |        |           |
|         rowid | STRING | true |     |        |           |
|       runtime |    INT | true |     |        |           |
|     starttime | STRING | true |     |        |           |
|    systemtime | STRING | true |     |        |           |
|   temperature | STRING | true |     |        |           |
|  temperaturef | STRING | true |     |        |           |
|            ts |    INT | true |     |        |           |
|          uuid | STRING | true |     |        |           |
+---------------+--------+------+-----+--------+-----------+
35 rows in set

select * from rp4enviroplus;

````

### Pulsar SQL

````
presto> select * from pulsar."public/default"."rp4enviroplus";

 adjtemp | adjtempf | amplitude100 | amplitude1000 | amplitude500 | amps | cpu | cputemp | cputempf | diskusage  |      endtime       |           gasko           | highnoise | host | hostname | humidity |   ipaddress   | lownoise | lux  |    macaddress     | memory | midnoise |  
---------+----------+--------------+---------------+--------------+------+-----+---------+----------+------------+--------------------+---------------------------+-----------+------+----------+----------+---------------+----------+------+-------------------+--------+----------+--
 26.7    | 60.1     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 45.7    | 114      | 31435.2 MB | 1646157120.7991426 | Oxidising: 19675.68 Ohms +|       0.2 | rp4  | rp4      |     16.3 | 192.168.1.209 |      0.4 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.1 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 119000.00 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 27355.89 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 26.9    | 60.4     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 46.2    | 115      | 31435.2 MB | 1646157122.9693346 | Oxidising: 20143.39 Ohms +|       0.2 | rp4  | rp4      |     16.3 | 192.168.1.209 |      0.6 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.4 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 120000.00 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 27923.71 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 26.5    | 59.7     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 46.2    | 115      | 31435.2 MB | 1646157125.1368313 | Oxidising: 20616.92 Ohms +|       0.2 | rp4  | rp4      |     16.3 | 192.168.1.209 |      0.4 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.2 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 120504.30 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 28383.56 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 26.6    | 59.9     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 45.7    | 114      | 31435.2 MB | 1646157127.3089767 | Oxidising: 21096.37 Ohms +|       0.2 | rp4  | rp4      |     16.3 | 192.168.1.209 |      0.5 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.3 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 121521.61 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 28965.52 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.3    | 61.1     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 45.7    | 114      | 31435.2 MB | 1646157129.478687  | Oxidising: 21581.86 Ohms +|       0.1 | rp4  | rp4      |     16.3 | 192.168.1.209 |      0.4 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.1 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 122034.68 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 29436.89 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.0    | 60.6     |          1.0 |           0.3 |          0.4 |  0.3 | 0.0 | 45.7    | 114      | 31435.2 MB | 1646157131.6498218 | Oxidising: 22073.51 Ohms +|       0.2 | rp4  | rp4      |     16.2 | 192.168.1.209 |      0.5 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.3 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 122550.72 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 29913.53 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.1    | 60.8     |          1.0 |           0.1 |          0.3 |  0.3 | 0.2 | 46.2    | 115      | 31435.2 MB | 1646157133.8205895 | Oxidising: 22471.34 Ohms +|       0.3 | rp4  | rp4      |     16.2 | 192.168.1.209 |      0.5 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.3 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 123591.84 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 30395.51 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.1    | 60.8     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 46.2    | 115      | 31435.2 MB | 1646157135.9879181 | Oxidising: 22873.24 Ohms +|       0.2 | rp4  | rp4      |     16.2 | 192.168.1.209 |      0.6 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.4 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 124116.96 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 30882.93 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.0    | 60.6     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 46.2    | 115      | 31435.2 MB | 1646157138.160729  | Oxidising: 23279.28 Ohms +|       0.2 | rp4  | rp4      |     16.1 | 192.168.1.209 |      0.4 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.2 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 124645.16 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 31252.12 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 26.9    | 60.4     |          1.1 |           0.4 |          0.4 |  0.3 | 0.0 | 46.2    | 115      | 31435.2 MB | 1646157140.3307676 | Oxidising: 23689.52 Ohms +|       0.0 | rp4  | rp4      |     16.1 | 192.168.1.209 |      0.4 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.1 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 125176.47 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 31749.29 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.1    | 60.8     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 45.7    | 114      | 31435.2 MB | 1646157142.5007892 | Oxidising: 24104.03 Ohms +|       0.4 | rp4  | rp4      |     16.0 | 192.168.1.209 |      0.4 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.3 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 125710.91 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 32125.89 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 26.9    | 60.4     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 47.2    | 117      | 31435.2 MB | 1646157144.669611  | Oxidising: 24522.88 Ohms +|       0.3 | rp4  | rp4      |     16.0 | 192.168.1.209 |      0.5 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.3 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 126248.52 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 32505.75 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.4    | 61.3     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 45.7    | 114      | 31435.2 MB | 1646157146.839814  | Oxidising: 24839.90 Ohms +|       0.1 | rp4  | rp4      |     16.0 | 192.168.1.209 |      0.4 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.1 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 126248.52 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 32888.89 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.0    | 60.6     |          1.0 |           0.3 |          0.4 |  0.3 | 0.0 | 46.2    | 115      | 31435.2 MB | 1646157149.008095  | Oxidising: 25159.42 Ohms +|       0.2 | rp4  | rp4      |     16.1 | 192.168.1.209 |      0.5 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.3 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 126789.32 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 33275.36 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.0    | 60.6     |          1.1 |           0.4 |          0.5 |  0.3 | 0.0 | 46.2    | 115      | 31435.2 MB | 1646157151.1756244 | Oxidising: 25481.48 Ohms +|       0.2 | rp4  | rp4      |     16.0 | 192.168.1.209 |      0.5 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.3 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 127333.33 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 33665.21 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 27.4    | 61.3     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 46.2    | 115      | 31435.2 MB | 1646157153.365354  | Oxidising: 25806.11 Ohms +|       0.1 | rp4  | rp4      |     16.0 | 192.168.1.209 |      0.4 | 55.0 | a2:3f:eb:35:a7:99 |    7.3 |      0.2 |  
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 127333.33 Ohms +|           |      |          |          |               |          |      |                   |        |          |  
         |          |              |               |              |      |     |         |          |            |                    | NH3: 34058.48 Ohms        |           |      |          |          |               |          |      |                   |        |          |  
 9.0     | 28.2     |          1.0 |           0.2 |          0.3 |  0.3 | 0.0 | 45.7    | 114      | 31435.2 MB | 1646156957.410107  | Oxidising: 466033.90 Ohms+|       0.6 | rp4  | rp4      |     16.3 | 192.168.1.209 |      0.4 | 55.9 | a2:3f:eb:35:a7:99 |    7.2 |      0.3 | 2
         |          |              |               |              |      |     |         |          |            |                    | Reducing: 4682461.54 Ohms+|           |      |          |          |               |          |      |                   |        |          |  
 
````

### References

* https://shop.pimoroni.com/products/enviro?variant=31155658457171
* https://www.datainmotion.dev/2019/12/iot-series-minifi-agent-on-raspberry-pi.html
* https://github.com/tspannhw/meetup-sensors
* https://github.com/tspannhw/minifi-enviroplus
