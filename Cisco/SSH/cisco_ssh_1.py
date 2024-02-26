# Python script that can be used to access cisco switch via SSH

# Import libraries
import paramiko
import getpass  # library to get pass details secretly
import time

# Login paramters
host = '192.168.193.143'
user = input('Username: ')
pwd = getpass.getpass('Password: ')

# Established Connection with login parameter
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, username=user, password=pwd)

print('Successfully connected to => ' + host)

# Send some cisco configuration
remote_conn = ssh_client.invoke_shell()
# remote_conn.send("enable\n")
# remote_conn.send("admin\n")
remote_conn.send("configure terminal\n")
remote_conn.send("vlan 2\n")
remote_conn.send("name vlan admin\n")
remote_conn.send("interface vlan 2\n")
remote_conn.send("ip address 2.2.2.2 255.0.0.0\n")
remote_conn.send("no shutdown\n")
remote_conn.send("end\n")
time.sleep(1)

# Get back an output
output = remote_conn.recv(6553)
print(output.decode('ascii'))

ssh_client.close()



# Terminal ssh connection or session
ssh_client.close
