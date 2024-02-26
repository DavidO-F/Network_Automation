# Author: David O. Folorunsho
# Date: 05/10/2023
# About: How to config a new mikrotik router for internet access
# Description: This program uses a prepared file that has config command already prepared
# Given: Public IP for WAN interface connection; Private IP for LAN interface connection
# Tasks: Router Identity, Configure Public IP, Configure Private IP, DHCP for LAN device, Bridge Interface and Port, Static Routing, Natinng, readonly access Interface graphing

# Import library
import paramiko
# print("Library imported")

# Open configuration file
config_file_handler = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Mikrotik/Mikrotik Automation with Python/enterprise_Service_config.txt')
# print("file read")
# print(file_handler)

# Establish connection to network device
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.193.130', username='admin', password='admin') # port=1522 for already configured
# print("Connection establish to mikrotik")

# Execute configurations
for line_config in config_file_handler:
    # print("Content of line: ")
    # print(line)
    cmd = line_config.strip('""\n')
    # print("Content of cmd: ")
    # print(cmd)
    stdin, stdout, stderr = client.exec_command(cmd)
    for res in stdout:
        print(res.strip('\n'))
print("Configuration Done")
client.close()