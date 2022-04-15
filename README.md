# DHT22 prometheus exporter

The DHT22 is a cheap "DIY" sensor for microcontrollers (arduino, rpi)

This repository creates a prometheus exporter so that metrics can be collected and displayed.

![Grafana graph of metrics collected](https://i.imgur.com/m7eCUPh.png)
View above dashboard json [here.](./grafana.json)

## Project Status

**This project is abandoned**. I don't write python anymore and don't work enough with the rpis strewn about my house to keep the motivation to keep updating things.

Please fork or migrate to more maintained repos.

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

- Raspberry pi 3
- [DHT22 Sensor](https://amzn.to/2m3Qelh)
  - The one linked above comes with built in resistor

### Install on Raspbian

- Copy the python file to the path you want to keep it. ex: `/usr/local/bin`
- Go to that path and install dependencies: `sudo pip3 install -r requirements.txt`
- Assuming the use of systemd, copy the service file at [dht22-exporter.service](./dht22-exporter.service) to /etc/systemd/system and daemon-reload systemd via `sudo systemctl daemon-reload`. You might want to also enable the service so that it persists after a reboot: `sudo systemctl enable dht22-exporter.service`.
- In this service file some default values for the pin and polling rate `Ex: ./dht22_exporter -g 4 -i 2`, change these values to align with what ever your board setup is.
- If you're not running systemd, figure out a way to run the python file continuously (through screen, as a service, etc).
- Start the dht22-exporter service and point prometheus on port 8001 (unless changed with parameter `-p/--port`).

### Known Issues

- The sensor sometimes gives wildly inaccurate readings (5000% humidity), this should be mitigated by some checks in the code, but ~1% of sensor readings may not be even close to accurate.

## Authors

- **Clint Edwards** - [Github](https://github.com/clintjedwards)
