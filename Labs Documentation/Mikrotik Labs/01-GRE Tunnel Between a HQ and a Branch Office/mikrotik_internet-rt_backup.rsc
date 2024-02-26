# 2024-01-10 20:52:40 by RouterOS 7.11.2
# software id = 
#
/interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik
/port set 0 name=serial0
/ip address add address=200.20.20.2/30 interface=ether1 network=200.20.20.0
/ip address add address=200.20.20.5/30 interface=ether2 network=200.20.20.4
/ip dhcp-client add interface=ether1
/system identity set name=Internet-RT
/system note set show-at-login=no
