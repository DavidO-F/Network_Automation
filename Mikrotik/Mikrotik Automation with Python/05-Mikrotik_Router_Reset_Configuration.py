# Author: David O. Folorunsho
# Date: 05/10/2023
# About: How to Reset Mikrotik Router configuration with python script
# Given/Required: IP Address; Username and Password port number
# Tasks: 

# Import library
import paramiko
# print("Library imported")


# Establish connection to network device
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.193.130', username='admin', password='admin', port=1522) # port=1522 for already configured
# print("Connection establish to mikrotik")

# Execute configurations
stdin, stdout, stderr = client.exec_command("/system reset")
stdin, stdout, stderr = client.exec_command("y")
print("Reset Configuration Done")
client.close()