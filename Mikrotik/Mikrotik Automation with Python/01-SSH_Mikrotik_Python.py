import requests
import json
import urllib3
urllib3.disable_warnings()
from requests.auth import HTTPBasicAuth

####################### Parameter Declaration #######################
url = 'https://192.168.193.130'
username = 'admin'
password = 'admin'

# ipaddr = input("Enter IP Address: ")
# usern = input("Enter your login Username: ")
# passW = input("Enter your Password: ")

# url = 'https://' + ipaddr + '/rest'


# resp = requests.get('https://196.1.179.154/rest/interface', auth=HTTPBasicAuth('admin', 'eStream2014'), verify=False)

# resp = requests.get('https://196.1.176.61/rest/interface', auth=HTTPBasicAuth('admin', 'mrk@eStream'), verify=False)

resp = requests.get(url + '/rest/interface', auth=HTTPBasicAuth(username, password), verify=False)
# resp = requests.get(url + '/interface', auth=HTTPBasicAuth(usern, passW), verify=False)

# resp = requests.get('http://196.1.179.154:8728/webfig/#IP:Addresses.Address.2', auth=HTTPBasicAuth('admin', 'eStream2014'), verify=False)

# print(type(resp))
# data = resp.text
# print(resp.raw)
# print(data)
# print(json.loads(data))
# print(resp.json())
# print(json.dumps(resp.json(), indent=4))

for interface in resp.json():
   print(interface["type"])

for interface in resp.json():
    if interface['type'] == 'bridge':
        print("The interface ID is: " + interface[".id"] + " interface type is " + interface["type"])

