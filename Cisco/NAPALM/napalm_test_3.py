#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

ip_addr = input("Enter IP Address: ")

device = { 
    'device_type': 'cisco_ios',
    'ip': ip_addr,
    'username': 'admin',
    'password': getpass(),
    # 'port' : 23,
} 
net_connect = ConnectHandler(**device)
output = net_connect.send_command("show ip int brief")
print(output)