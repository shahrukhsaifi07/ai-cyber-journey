import socket

target =input("Enter target (e.g. google.com): ")
start_port=int(input("Start port :"))
end_port=int(input("End port :"))
common_ports = [21, 22, 80, 443, 3306, 8080]
choice =input("Scan commong ports only? (y/n):")
open_ports=[]

def scan_port(target,port):
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.settimeout(1)

     result=s.connect_ex((target,port))
     s.close()

     return result == 0

if choice == "y":
     ports=common_ports
     for port in ports:
         if scan_port(target,port):
             print(f"[OPEN] {port}")
             open_ports.append(port)
        # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # s.settimeout(1)

        # result=s.connect_ex((target,port))

        # if result ==0:
        #     print(f"[OPEN] Port {port}")
        #     open_ports.append(port)
        
        # s.close()

else:
    ports =range(start_port,end_port + 1)
    for port in  ports:
       if scan_port(target,port):
           print(f"[OPEN] {port}")
           open_ports.append(port)
         
        
       

print("Open Ports:",open_ports)
print("Total Open Ports:",len(open_ports))





   