import paramiko
# print("Library imported")

file_handler = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Mikrotik/Mikrotik Automation with Python/mikrotik_print_commands.txt')
# print("file read")
# print(file_handler)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.193.130', username='admin', password='admin')
print("Connection establish to mikrotik")


for line in file_handler:
    print("Content of line: ")
    print(line)
    cmd = line.strip('""\n')
    print("Content of cmd: ")
    print(cmd)
    stdin, stdout, stderr = client.exec_command(cmd)
    for res in stdout:
        print(res.strip('\n'))
print("about to abort")
client.close()


