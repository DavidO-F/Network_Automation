# Define the required libraries
import telnetlib

# Define the require variables
# host_ip = '192.168.193.137'
host_ip = "192.168.193.142"
username = 'admin'
password = 'admin'

# Using the info (IP, Username and password) to telnet into the Router
tn = telnetlib.Telnet(host_ip)

# Handle the Username/Password prompt and supply our values
tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b'\n')
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b'\n')

# Execute some command on the router by Write
tn.write(b'ena\n')
tn.write(b'admin\n')
tn.write(b'config term\n')
tn.write(b'int loop 0\n')
tn.write(b'ip address 10.10.10.10 255.255.255.255\n')
tn.write(b'int loop 1\n')
tn.write(b'ip address 20.20.20.20 255.255.255.255\n')
tn.write(b'end\n')
tn.write(b'exit\n')

# Generate command line configuration: Print out what we have done on the device-Router with this command
print(tn.read_all().decode())