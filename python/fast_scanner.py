import socket
import threading
from threading import Semaphore

thread_limit = Semaphore(50)

target= input("Enter target:")
ports= range(1,100)

open_ports=[]

def scan_port(port):
    with thread_limit:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)

        result=s.connect_ex((target,port))

        if result ==0:
            print(f"[OPEN] {port}")
            open_ports.append(port)

        s.close()

threads = []

for port in ports:
    t=threading.Thread(target=scan_port,args=(port,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print("Open Ports :", open_ports)


