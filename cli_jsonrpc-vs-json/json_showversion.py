#!/usr/bin/python3

import requests
import json

requests.packages.urllib3.disable_warnings()

host = 'sbx-nxos-mgmt.cisco.com'
username = 'admin'
password = 'Admin_1234!'
authentication = (username, password)

url='https://{}:443/ins'.format(host)

myheaders={'content-type':'application/json'}

payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show version",
    "output_format": "json"
  }
}

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=authentication, verify=False).json()

result = response['ins_api']['outputs']['output']['body']
#for k,v in result.items():
#	print(f'{k} -  {v}')

print(f'Hostname: {result["host_name"]}')
print(f'Chassis: {result["chassis_id"]}')
print(f'Version: {result["nxos_ver_str"]}')
