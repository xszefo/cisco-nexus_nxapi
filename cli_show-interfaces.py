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
      "cmd": "show interface",
      "version": 1
    },
    "id": 1
  }
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=authentication, verify=False).json()

result = response['result']['body']['TABLE_interface']['ROW_interface']

for iface in result:
	name = iface.get('interface', 'unknown')
	state = iface.get('state', 'unknown')
	mtu = iface.get('eth_mtu', 'unknown')

	print(f'{name} is {state} | MTU: {mtu}')

