import socket
import threading
from threading import Semaphore

thread_limit = Semaphore(50)

target= input("Enter target:")
ports=range(1,101)

open_ports=[]

port_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}
 
def scan_port(port):
    with thread_limit:
        s=socket.socket()
        s.settimeout(1)

        try:
            s.connect((target,port))
            service = port_services.get(port,"Unknown")

            print(f"[OPEN] {port} -> {service}")

            try:
                banner=s.recv(1024).decode().strip()
                print(f" Service : {banner}")
            except:
                print(".  No banner")

            open_ports.append(port)
        except:
            pass

        s.close() 

        # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # s.settimeout(1)

        # result=s.connect_ex((target,port))

        # if result ==0:
        #     print(f"[OPEN] {port}")
        #     open_ports.append(port)

        # s.close()

threads = []

for port in ports:
    t=threading.Thread(target=scan_port,args=(port,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print("Scanning completed!")
# print("Open Ports :", open_ports)
print("Total Open Ports :", len(open_ports))


