#!/usr/bin/python3

import requests
import json

requests.packages.urllib3.disable_warnings()

host = 'sbx-nxos-mgmt.cisco.com'
username = 'admin'
password = 'Admin_1234!'

auth_body = {
	"aaaUser": {
		"attributes": {
    		"name": username, 
			"pwd": password
		}
	}
}

base_url='https://{}:443/api/'.format(host)
login = 'aaaLogin.json'
system = 'api/mo/sys.json'

##############################
######## LOGGING IN ##########
##############################
auth_url = base_url + login

auth_response = requests.post(auth_url, json=auth_body, timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']

##############################
########## VERSION ###########
##############################
cookies = {
		'APIC-Cookie': token
}

headers = {"content-type": "application/json"}
system_url = base_url + system

#print(version_url)

response = requests.get(url=system_url, headers=headers, cookies=cookies, verify=False)

sys_info = response.json()["imdata"][0]["topSystem"]["attributes"]

print("HOSTNAME:", sys_info["name"])
print("SERIAL NUMBER:", sys_info["serial"])
print("UPTIME:", sys_info["systemUpTime"])

