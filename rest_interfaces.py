#!/usr/bin/python3

import requests
import json

requests.packages.urllib3.disable_warnings()

host = 'sbx-nxos-mgmt.cisco.com'
username = 'admin'
password = 'Admin_1234!'

auth_body = {"aaaUser": {"attributes": {
    "name": username, "pwd": password}}}

base_url='https://{}:443/api/'.format(host)
login = 'aaaLogin.json'
interfaces = 'node/mo/sys/intf.json?query-target=children'

##############################
######## LOGGING IN ##########
##############################
auth_url = base_url + login

auth_response = requests.post(auth_url, json=auth_body, timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']

##############################
######## INTERFACES ##########
##############################
cookies = {
		'APIC-Cookie': token
}

headers = {"content-type": "application/json"}
interfaces_url = base_url + interfaces

response = requests.get(url=interfaces_url, headers=headers, cookies=cookies, verify=False)

resp_json = response.json()['imdata']

for interface in resp_json:
	try:
		attrs = list(interface.values())
		details = attrs[0]['attributes']
		name = details.get('id', 'none')
		adminState = details.get('adminSt', 'none')
		mode = details.get('mode', 'none')
		mtu = details.get('mtu', 'none')
		print(f'{name} ({adminState}) | {mode} | MTU: {mtu}')

	except Exception as err:
		print('Error')
		print(err)
		break	
