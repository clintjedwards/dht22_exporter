# DHT22 prometheus exporter

The DHT22 is a cheap "DIY" sensor for microcontrollers (arduino, rpi)

![Grafana graph of metrics collected](https://i.imgur.com/m7eCUPh.png)

## Example of exported metrics

```
...
# HELP dht22_temperature_celsius Temperature in celsius provided by dht sensor
# TYPE dht22_temperature_celsius gauge
dht22_temperature_celsius 22.8
# HELP dht22_temperature_fahrenheit Temperature in fahrenheit provided by dht sensor
# TYPE dht22_temperature_fahrenheit gauge
dht22_temperature_fahrenheit 73.0
# HELP dht22_humidity Humidity in percents provided by dht sensor
# TYPE dht22_humidity gauge
dht22_humidity 48.8
```

## Local Testbed

* Raspberry pi 3
* [DHT22 Sensor](https://amzn.to/2m3Qelh)
    * The one linked above comes with built in resistor

### Install on Linux
* Copy the python file to some where in your path. ex: `/usr/local/bin`
* Go to this path and install dependancies: `sudo pip install -r requirements.txt`
* Assuming the use of systemd, copy the service file to /etc/systemd/system and daemon-reload systemd. You might want to also enable the service so that it persists after a reboot.
* If you're not running systemd, figure out a way to run the python file continuously (through screen, as a service, etc).
* Start the dht22-exporter service and point prometheus at port 8001.

### Known Issues
* The sensor sometimes gives wildly inaccurate readings (5000% humidity), this should be mitigated by some checks in the code, but ~1% of sensor readings may not be even close to accurate.

## Authors

- **Clint Edwards** - [Github](https://github.com/clintjedwards)
