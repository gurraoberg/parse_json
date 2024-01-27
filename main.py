#!/bin/python

import json

with open('json/data.json', 'r') as file:
     data = json.load(file)

distro_list = data['distro']

for distro in distro_list:
     hostname = distro['hostname']
     system = distro['system']
     version = distro['version']

     print(f"Hostname: {hostname}\nSystem: {system}\nVersion: {version}\n")