import socket

target ="google.com"
ports = [21, 22, 80, 443, 8080]

open_ports=[]

for port in ports:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)

    result=s.connect_ex((target,port))

    if result ==0:
         open_ports.append(port)
     
    s.close()

print("Open Ports:",open_ports)

  
