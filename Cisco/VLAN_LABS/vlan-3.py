# Date: 28-09-2023
# Author: David O. Folorunsho
# Telnet with Python in to a Cisco switch in EVE NG environment


# Define the required libraries
import telnetlib
import getpass

# Define the require variables
# host_ip = '192.168.193.137'
host_ip = "192.168.193.130"

# Direct parameter supply
# username = 'admin'
# password = 'admin'

# Direct command line parameter supply
# username = input("Enter your Telnet Username: ")
# password = input("Enter your Telnet Password: ")

# Command line secret way to provide credential
username = getpass.getpass("Enter your Telnet Username: ")
password = getpass.getpass("Enter your Telnet Password: ")

# Using the info (IP, Username and password) to telnet into the Router
tn = telnetlib.Telnet(host_ip)

# Handle the Username/Password prompt and supply our values
tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b'\n')
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b'\n')

# Execute some command on the router by Write
tn.write(b'enable\n')
tn.write(b'admin\n')
tn.write(b'configure terminal\n')

# Create vlan with for loop
for n in range(51, 101):
    k = str(n)
    tn.write(b'vlan ' + k.encode('ascii') + b'\n')      # create vlan
    tn.write(b'name VLAN_' + k.encode('ascii') + b'\n')      # name vlan

tn.write(b'end\n')
tn.write(b'exit\n')

# Generate command line configuration: Print out what we have done on the device-Router with this command
print(tn.read_all().decode())