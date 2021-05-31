#!/usr/bin/env python3

# Prometheus exporter for DHT22 running on raspberrypi
# Usage: ./dht22_exporter -g <gpio_pin_number> -i <poll_time_in_seconds> [-p <exposed_port>]
# Ex: ./dht22_exporter -g 4 -i 2

import time
import argparse

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


def read_sensor(pin):
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gpio", dest="gpio", type=int, 
                        required=True, help="GPIO pin number on which the sensor is plugged in")
    parser.add_argument("-i", "--interval", dest="interval", type=int, 
                        required=True, help="Interval sampling time, in seconds")
    parser.add_argument("-p", "--port", dest="port", type=int, default=8001, 
                        required=False, help="Port that will be exposed")

    args = parser.parse_args()

    start_http_server(args.port)

    while True:
        read_sensor(pin=args.gpio)
        time.sleep(int(args.interval))


main()
