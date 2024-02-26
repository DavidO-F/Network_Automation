# By: David O. Folorunsho
# Date: 04/10/2023
# Title: Backup cisco devices configuration to file
# Lab type: Virtual Lab
# Lab environment: eve ng


#  Define the require libraries
import telnetlib
import getpass

# Define the require variables
user = input('Enter your username: ')
pwd = getpass.getpass('Enter your password: ')

# open file.txt to read IP address for user login
# file_handler = open('SW_IP_FILE.txt')   # Relative path

# Full file path
file_handler = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Cisco/TELNET_LABS/SW_IP_FILE.txt')

# Telnet with the obtain information
for line in file_handler:
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
    tn.write(b'show run\n')
    tn.write(b'exit\n')


# Generate command line configuration: Print out what we have done on the device-Router with this command
    print(tn.read_all().decode())