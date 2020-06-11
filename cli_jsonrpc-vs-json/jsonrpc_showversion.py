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
      "cmd": "show version",
      "version": 1
    },
    "id": 1
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=authentication, verify=False).json()

result = response['result']['body']
#for k,v in result.items():
#	print(f'{k} - {v}')

print(f'Hostname: {result["host_name"]}')
print(f'Chassis: {result["chassis_id"]}')
print(f'Version: {result["nxos_ver_str"]}')
