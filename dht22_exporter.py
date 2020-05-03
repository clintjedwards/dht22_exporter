#!/usr/bin/env python

# Prometheus exporter for DHT22 running on raspberrypi
# Usage: ./dht22_exporter <pin_number> <poll_time_in_seconds>
# Ex: ./dht22_exporter 4 2

import sys
import time

from prometheus_client import Gauge, start_http_server

import Adafruit_DHT

# Create a metric to track time spent and requests made.
dht22_temperature_celsius = Gauge(
    'dht22_temperature_celsius', 'Temperature in celsius provided by dht sensor')
dht22_temperature_fahrenheit = Gauge(
    'dht22_temperature_fahrenheit', 'Temperature in fahrenheit provided by dht sensor')
dht22_humidity = Gauge(
    'dht22_humidity', 'Humidity in percents provided by dht sensor')

SENSOR = Adafruit_DHT.DHT22


def read_sensor():
    pin = sys.argv[1]

    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, pin)

    if humidity is None or temperature is None:
        return

    if humidity > 200 or temperature > 200:
        return

    dht22_humidity.set('{0:0.1f}'.format(humidity))
    dht22_temperature_fahrenheit.set(
        '{0:0.1f}'.format(9.0/5.0 * temperature + 32))
    dht22_temperature_celsius.set(
        '{0:0.1f}'.format(temperature))


def main():
    start_http_server(8001)

    while True:
        read_sensor()
        time.sleep(int(sys.argv[2]))


main()
