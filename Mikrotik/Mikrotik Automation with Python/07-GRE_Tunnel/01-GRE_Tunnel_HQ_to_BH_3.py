# Author: David O. Folorunsho
# Date: 10/10/2023
# About: How to config GRE tunnel between HQ and Branch office
# Description: This program uses a prepared file that has configurations command already prepared and tested on mikrotik
# Given: Public IP for WAN interface connection; Private IP for LAN interface connection
# Tasks: Router Identity, 

# Import library
import paramiko
# print("Library imported")

# Node(Mikrotik) IP addresses
# HQ_MKT = "192.168.193.130"
# ISP_PE_HQ = "192.168.193.140"
# ISP_PE_BH = "192.168.193.143"
# BH_MKT = "192.168.193.144"

# Open configuration file
config_file_HQ_MKT = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Mikrotik/Mikrotik Automation with Python/07-GRE_Tunnel/MRK_1_HQ_MKT.txt')
config_file_ISP_PE_HQ = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Mikrotik/Mikrotik Automation with Python/07-GRE_Tunnel/MRK_2_ISP_PE_HQ.txt')
config_file_ISP_PE_BH = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Mikrotik/Mikrotik Automation with Python/07-GRE_Tunnel/MRK_2_ISP_PE_BH.txt')
config_file_BH_MKT = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Mikrotik/Mikrotik Automation with Python/07-GRE_Tunnel/MRK_4_BH_MKT.txt')
config_node_handler = open('C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Labs/Mikrotik/Mikrotik Automation with Python/07-GRE_Tunnel/Node_IP_Address_List.txt')
config_files = open()

for line_node,line_config in config_node_handler,config_files:
    node_add = line_node.strip('\n')
    line_con = line_config.strip('\n')
    config_file_HQ_MKT = open("'C:/Users/DFolorunsho/Documents/DAVID@ESN/Python/PythonNet/PyNet3/Laline_conbs/Mikrotik/Mikrotik Automation with Python/07-GRE_Tunnel/" +  + "'")

# Establish connection to network device
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.193.130', username='admin', password='admin')
# print("Connection establish to mikrotik")

# Execute configurations
for line_config in config_node_handler:
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