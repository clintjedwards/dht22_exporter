from io import open
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='dht22_exporter',
    version='2021-09-05',
    install_requires=requirements,
    packages=find_packages(),
    scripts=['dht22_exporter.py'],
)
