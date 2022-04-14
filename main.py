import platform
import socket
import os

username = os.getlogin()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print (username)
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print("Windows : " + platform.system() , platform.release())
print("Windows version : " + platform.version())
