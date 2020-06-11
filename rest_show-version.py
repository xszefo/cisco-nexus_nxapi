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
version = 'node/mo/sys/showversion.json?query-target=self'
#version = 'node/mo/sys/showversion.json'

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
version_url = base_url + version

#print(version_url)

response = requests.get(url=version_url, headers=headers, cookies=cookies, verify=False)

resp_json = response.json()['imdata'][0]['sysmgrShowVersion']['attributes']

uptime = resp_json['kernelUptime'].strip()
version = resp_json['nxosVersion'].strip()

print(f'{host} is alive for {uptime} and it is running NXOS {version}')

#for k,v in resp_json.items():
#	print(f'{k} - {v}')
#
#kernelUptime - 2 hour(s) 32 minute(s) 9 second(s)
#lastResetReason - Unknown
#lastResetService -
#lastResetSysVersion -
#lastResetTime -
#nxosCompileTime -  12/22/2019 2:00:00
#nxosImageFile - bootflash:///nxos.9.3.3.bin
#nxosVersion - 9.3(3)
#plugin - Core Plugin, Ethernet Plugin

