import datetime
import os
import subprocess
import telnetlib
import time

username = "cisco"
unamepw = "telnetpassword"
ip = "192.168.1.254"

tn = telnetlib.Telnet(ip)
time.sleep(2)
response = tn.read_until(b"User Name:", 5)
print(response)

if b"User Name:" in response:
	print("found")
	tn.write(username.encode('ascii') + b"\n")
	output = tn.read_until(b":", 5)
	print(output)
	tn.write(unamepw.encode('ascii') + b"\n")
	output = tn.read_until(b"#", 5)
	print(output)
	
else:
	print("not found")
	tn.write(telnetpw.encode('ascii') + b"\n")
	tn.read_until(b">", 5)

tn.write(b"configure terminal" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"hostname residence-sw" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"vlan 20" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"exit" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"spanning-tree vlan 20 root primary" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"int e1/0" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"switchport mode access" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"switchport access vlan 20" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"sh run" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.close()


                    
