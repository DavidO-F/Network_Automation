import ipaddress

# ip_addr1 = ipaddress.ip_address('196.1.176.61') # example of private IP address

# ip_addr1 = ipaddress.ip_address('100.1.176.61') # example of public/global IP address

# ip_addr1 = ipaddress.ip_address('169.254.0.1')  # example of link local address

ip_addr1 = ipaddress.ip_address('127.0.0.1') # example of loopback IP address

# ip_addr1 = ipaddress.ip_address(input("Enter an IP: "))

print(f"IP Address provided is: {ip_addr1}")

print(type(ip_addr1))

print(dir(ip_addr1))

print(ip_addr1.max_prefixlen)

print(ip_addr1.reverse_pointer)

exp = ip_addr1.exploded 

print(f'Print expload var: {exp}')

print(f'Print expload type: {type(exp)}')

print(f"Is IP address a multicaslt?: {ip_addr1.is_multicast}")

print(f"Is IP address a private?: {ip_addr1.is_private}")

print(f"Is IP address a global?: {ip_addr1.is_global}")

print(f"Checking for IP Link local: {ip_addr1.is_link_local}")

print(f"Is IP address a loopback?: {ip_addr1.is_loopback}")

try:
    ip_addr2 = ipaddress.ip_address(input("Enter IP: "))

except ValueError:
    print("Invalid IP")