#!/bin/python

import json

with open('json/data.json', 'r') as file:
     data = json.load(file)

distro_list = data['distro']
hostname_list = []


for distro in distro_list:
     hostname = distro['hostname']
     system = distro['system']
     version = distro['version']

     hostname_list.append(hostname)

     print(f"Hostname: {hostname}\nSystem: {system}\nVersion: {version}\n")


total_hosts = 0
print("\033[4mHostnames:\033[0m")
for hostname in hostname_list:
     total_hosts +=1
     print(hostname)
print(f"Total hosts: {total_hosts}")