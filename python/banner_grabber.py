import socket

target=input("Enter target :")
port=int(input("Enter port:"))

s=socket.socket()
s.settimeout(2)

try:
    s.connect((target,port))
    banner=s.recv(1024)
    print("Banner :",banner.decode().strip())
except:
    print("No banner or connection failed")

s.close()