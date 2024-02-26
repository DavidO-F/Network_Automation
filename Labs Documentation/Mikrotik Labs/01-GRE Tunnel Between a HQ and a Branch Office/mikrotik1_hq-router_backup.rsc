# 2024-01-10 21:07:12 by RouterOS 7.11.2
# software id = 
#
/interface gre add comment="GRE Tunnel Interface for HQ" local-address=200.20.20.1 name=to-branch remote-address=200.20.20.6
/interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik
/ip pool add name=dhcp_pool0 ranges=192.168.10.2-192.168.10.254
/ip dhcp-server add address-pool=dhcp_pool0 interface=ether1 name=dhcp1
/port set 0 name=serial0
/ip address add address=192.168.10.1/24 comment="LAN INTERFACE" interface=ether1 network=192.168.10.0
/ip address add address=200.20.20.1/30 comment="WAN INTERFACE" interface=ether2 network=200.20.20.0
/ip address add address=10.10.10.1/30 comment="Tunnel Interface to the Branch" interface=to-branch network=10.10.10.0
/ip dhcp-client add interface=ether1
/ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1
/ip route add check-gateway=ping comment="Tunnel route to Branch LAN" disabled=no distance=1 dst-address=192.168.20.0/24 gateway=10.10.10.2 pref-src="" routing-table=main scope=30 suppress-hw-offload=no target-scope=10
/ip route add check-gateway=ping comment="Route to Internet" disabled=no distance=1 dst-address=0.0.0.0/0 gateway=200.20.20.2 pref-src="" routing-table=main scope=30 suppress-hw-offload=no target-scope=10
/system identity set name=HQ-Router
/system note set show-at-login=no
/tool graphing interface add interface=to-branch
