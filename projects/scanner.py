import socket
import threading
from threading import Semaphore

def port_scanner(target):
    # target = input("Enter target: ")
    ports = range(1, 101)

    thread_limit = Semaphore(50)
    open_ports = []

    port_services = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    }

    def scan_port(port):
        with thread_limit:
            s = socket.socket()
            s.settimeout(1)

            try:
                s.connect((target, port))
                service = port_services.get(port, "Unknown")

                # print(f"[OPEN] {port} → {service}")

                # try:
                #     banner = s.recv(1024).decode().strip()
                #     print(f"   ↳ Banner: {banner}")
                # except:
                #     print("   ↳ No banner")

                open_ports.append(f"{port} ({service})")

            except:
                pass

            s.close()

    threads = []

    # print("\nScanning...\n")

    for port in ports:
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    return open_ports

    # print("\nScanning completed!")
    # print("Total Open Ports:", len(open_ports))