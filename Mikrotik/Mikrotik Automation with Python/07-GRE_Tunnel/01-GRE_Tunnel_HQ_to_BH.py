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
HQ_MKT = "192.168.193.130"
ISP_PE_HQ = "192.168.193.140"
ISP_PE_BH = "192.168.193.143"
BH_MKT = "192.168.193.144"

# Login credential
user= "admin"
pwd = "admin"

# Pure Mikrotik Script
# Script For Headquater (HQ) Router
HQ_MRK_RB_ID = "/system identity set name=HQ-MKT"
HQ_MKT_IP_2 = "/ip address add address=192.168.2.1/24 interface=ether2 comment='HQ LAN interface Gateway IP Address'"
HQ_MKT_IP_3 = "/ip address add address=172.16.1.1/30 interface=ether3 comment='HQ WAN interface IP Address'"
HQ_MKT_GRE = "/interface gre add name=HQ-GRE-Interface local-address=172.16.1.1 remote-address=172.16.1.10 comment='GRE logical connection to Branch'"
HQ_MKT_IP_GRE = "/ip address add add=192.168.10.2/30 int=HQ-GRE-Interface comm='GRE Interface IP Address'"
HQ_MKT_GRE_ROUTE = "/ip route add dst=192.168.1.0/24 gat=192.168.10.1 com='GRE route' check-gateway=ping"
HQ_MKT_INT_ROUTE = "/ip route add gateway=172.16.1.2 check-gateway=ping dst-address=0.0.0.0/0 comment='Internet Route'"

# Script for Branch (BH) router
BH_MRK_RB_ID = "/system identity set name=BH-MKT"
BH_MRK_IP_3 = "/ip/address add address=192.168.1.1/24 interface=ether3 comment='Branch LAN Interface Gateway IP Address'"
BH_MRK_IP_2 = "/ip/address add address=172.16.1.10/30 interface=ether2 comment='Branch WAN Interface IP Address'"
BH_MKT_INT_ROUTE = "/ip/route add gateway=172.16.1.9 check-gateway=ping dst-address=0.0.0.0/0 comment='Internet Route'"
BH_MKT_GRE = "/interface/gre add name=BH-GRE-Interface local-address=172.16.1.10 remote-address=172.16.1.1 comment='GRE logical connection to HQ'"
BH_MKT_IP_GRE = "/ip/address add address=192.168.10.1/30 interface=BH-GRE-Interface comment='GRE Interface IP Address'"
BH_MKT_GRE_ROUTE = "/ip/route add dst=192.168.2.0/24 gat=192.168.10.2 check-gateway=ping com='GRE route'"

# Script for Provider Edge Router at HQ
PE_HQ_ID = "/system identity set name=ISP-PE-HQ"
PE_HQ_IP_2 = "/ip/address add address=172.16.1.2/30 interface=ether2 comment='Connection to HQ-MKT'"
PE_HQ_IP_3 = "/ip/address add address=172.16.1.5/30 interface=ether3 comment='Connection to ISP-PE-BH'"
PE_HQ_ROUTE = "/ip/route add dst-address=0.0.0.0/0 gateway=172.16.1.6 check-gateway=ping comment='Default route to any destination'"

# Script for Provider Edge Router at BH
PE_BH_ID = "/system identity set name=ISP-PE-BH"
PE_BH_IP_3 = "/ip address add address=172.16.1.6/30 interface=ether3 comment='Connection to ISP-PE-HQ'"
PE_BH_IP_2 = "/ip address add address=172.16.1.9/30 interface=ether2 comment='Connection to BH-MKT'"
PE_BH_ROUTE = "/ip/route add dst-address=0.0.0.0/0 gateway=172.16.1.5 check-gateway=ping comment='Default route to any destination'"

# Establish connection to network device
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(HQ_MKT, username=user, password=pwd)

# conf_list = (HQ_MRK_RB_ID, HQ_MKT_IP_2, HQ_MKT_IP_3, HQ_MKT_GRE, HQ_MKT_IP_GRE, HQ_MKT_GRE_ROUTE, HQ_MKT_INT_ROUTE)
HQ_CONFIG = (HQ_MRK_RB_ID, HQ_MKT_IP_2, HQ_MKT_IP_3, HQ_MKT_GRE, HQ_MKT_IP_GRE, HQ_MKT_GRE_ROUTE, HQ_MKT_INT_ROUTE)
BH_CONFIG = (BH_MRK_RB_ID, BH_MRK_IP_3, BH_MRK_IP_2, BH_MKT_INT_ROUTE, BH_MKT_GRE, BH_MKT_IP_GRE, BH_MKT_GRE_ROUTE)
IPS1_CONFIG = (PE_HQ_ID, PE_HQ_IP_2, PE_HQ_IP_3, PE_HQ_ROUTE)
ISP2_CONFIG = (PE_BH_ID, PE_BH_IP_3, PE_BH_IP_2, PE_BH_ROUTE)

# Route Tulp of IP and Config
R1 = (HQ_MKT, HQ_CONFIG)
R2 = (BH_MKT, BH_CONFIG)
R3 = (ISP_PE_HQ, IPS1_CONFIG)
R4 = (ISP_PE_BH, ISP2_CONFIG)

R_List = (R1, R2, R3, R4)

conf_list =(HQ_CONFIG, BH_CONFIG, IPS1_CONFIG, ISP2_CONFIG)
R_IP_LIST = (HQ_MKT, BH_MKT, ISP_PE_HQ, ISP_PE_BH)
# Execute configurations
for R, conf in R_List:
    # print(R)
    # print("Router List: " + R)
    # print("List of Configs: " + conf)
    # print(conf)
    # Establish connection to network device
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(R, username=user, password=pwd)
    for con in conf:
        # print("Router Config= " + con)
        print(con)
#         # print("\n")
#         # stdin, stdout, stderr = client.exec_command(cmd)
#         for R_CON in conf:
#             print(R_CON)
    print("\n")

# print("Configuration Done")
# client.close()

