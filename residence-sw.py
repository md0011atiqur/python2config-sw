import datetime
import os
import subprocess
import telnetlib
import time

username = "cisco"
unamepw = "cisco"
ip = "192.168.1.254"

tn = telnetlib.Telnet(ip)
time.sleep(2)
response = tn.read_until(b":", 5)
print(response)

if b"Username" in response:
	print("found")
	tn.write(username.encode('ascii') + b"\n")
	output = tn.read_until(b":", 5)
	print(output)
	tn.write(unamepw.encode('ascii') + b"\n")
	output = tn.read_until(b">", 5)
	print(output)
	tn.write(b"enable" + b"\n")
	output = tn.read_until(b":", 5)
	print(output)
	tn.write(unamepw.encode('ascii') + b"\n")
	output = tn.read_until(b"#", 5)
	print(output)
	
else:
	print("not found")

#tn.write(b"show vlan" + b"\n")
#output = tn.read_until(b"#", 5)
#print(output)

tn.write(b"configure terminal" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"vlan 222" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"end" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"show vlan" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.close()


                    
