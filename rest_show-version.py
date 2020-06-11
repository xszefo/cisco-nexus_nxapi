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

auth_url = base_url + login

auth_response = requests.post(auth_url, json=auth_body, timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']

cookies = {
		'APIC-Cookie': token
}
headers = {"content-type": "application/json"}

version_url = base_url + version
print(version_url)

response = requests.post(version_url, headers=headers, cookies=cookies, verify=False)
print(response)
print(response.text)
