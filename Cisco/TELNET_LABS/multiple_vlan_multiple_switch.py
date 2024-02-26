# By: David O. Folorunsho
# Date: 04/10/2023
# Title: Creating multiple VLAN on multiple switches
# Lab type: Virtual Lab
# Lab environment: eve ng


#  Define the require libraries
import telnetlib
import getpass

# Define the require variables
user = input('Enter your username: ')
pwd = getpass.getpass('Enter your password: ')

# open file.txt to read IP address for user login
# file_handler = open('SWIPFILE.txt')
file_handler = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Cisco/TELNET_LABS/SW_IP_FILE.txt')
print(file_handler)

# Telnet with the obtain information
for line in file_handler:
    print("Content of line: ")
    print(line)
    host_ip = line.strip('\n')
    print("Telnet to host: " + host_ip)
    tn = telnetlib.Telnet(host_ip)

# Handle the Username/Password prompt and supply our values
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b'\n')
    if pwd:
        tn.read_until(b"Password: ")
        tn.write(pwd.encode('ascii') + b'\n')

# Execute some command on the devices
    tn.write(b'ena\n')
    tn.write(b'admin\n')
    tn.write(b'configure terminal\n')

# Create vlan with for loop
    for n in range(20, 41):
        k = str(n)
        tn.write(b'vlan ' + k.encode('ascii') + b'\n')      # create vlan
        tn.write(b'name VLAN_' + k.encode('ascii') + b'\n')      # name vlan

    tn.write(b'end\n')
    tn.write(b'exit\n')


# Generate command line configuration: Print out what we have done on the device-Router with this command
    print(tn.read_all().decode())