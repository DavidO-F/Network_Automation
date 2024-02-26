import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('196.1.176.61', username='admin', password='mrk@eStream', port=1522)
# stdin, stdout, stderr = client.exec_command('ip address print')
stdin, stdout, stderr = client.exec_command('int pr')

for line in stdout:
    print(line.strip('\n'))
client.close()