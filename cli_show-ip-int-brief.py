#!/usr/bin/python3

import requests
import json

requests.packages.urllib3.disable_warnings()

host = 'sbx-nxos-mgmt.cisco.com'
username = 'admin'
password = 'Admin_1234!'
authentication = (username, password)

url='https://{}:443/ins'.format(host)

myheaders={'content-type':'application/json-rpc'}

payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show ip int brief",
      "version": 1
    },
    "id": 1
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=authentication, verify=False).json()

result = response['result']['body']['TABLE_intf']['ROW_intf']

#{'vrf-name-out': 'default', 'intf-name': 'Vlan103', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': 4, 'prefix': '172.16.103.1', 'ip-disabled': 'FALSE'}

for iface in result:
	print(f'{iface["intf-name"]} - {iface["prefix"]}')



