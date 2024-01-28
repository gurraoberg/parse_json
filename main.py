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

# Generate 100 new entries for testing.
last_index = len(data['distro'])
for i in range(last_index + 1, last_index + 101):
     new_json_data = {
          "hostname": f"hostname{i}",
          "system": "RHEL",
          "version": "8.8"
     }
     data['distro'].append(new_json_data)

with open('json/data.json', 'w') as file:
     json.dump(data, file, indent=2)
print("Added 100 new entries into 'data.json'.")
print(f"Total hosts: {len(hostname_list)}")