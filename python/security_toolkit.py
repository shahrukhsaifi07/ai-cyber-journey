import socket
import threading
from threading import Semaphore
import requests


#  Fast Scanner File
def port_scanner():
    target=input("Enter target :")
    ports = range(1,101)
    thread_limit = Semaphore(50)
    open_ports =[]

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
                service=port_services.get(port,"Unknown")
                print(f"[OPEN] {port} {service}")
                try:
                    banner=s.recv(1024).decode().strip()
                    print(f" Banner : {banner}")
                except:
                    print("No Banner")
                open_ports.append(port)
            except:
                pass

            s.close()


    threads=[]

    print("\nScanning ...\n")

    for port in ports:
        t=threading.Thread(target=scan_port,args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("\nScanning completed!")
    print("Total Open Ports :", len(open_ports))


# Brute force Login

def brute_force():
    url=input("Enter login URL:")
    username=input("Enter username")
    try:
        with open("password.txt","r") as file:
            passwords =file.readlines()
    except:
        print("password.txt file no found!")
        return
    
    for pwd in passwords:
        pwd=pwd.strip()


        data ={
            "username":username,
            "password":pwd
        }
        try:
            response = requests.post(url,data=data)
            print(f"Tried: {pwd} | Length : {len(response.text)}")
            if "success" in response.text.lower():
                print(f"\nPassword Found:{pwd}")
                break
        except:
            print("Request Failed")


# Log Analyzer


def log_analyzer():
    try:
        with open("logs.txt","r") as file:
            logs=file.readlines()
    except:
        print("Logs.txt file not found!")
        return
    
    failed=0
    success=0
    user_attempts={}

    for log in logs:
        if "Failed" in log:
            failed +=1

            try:
                user =log.split()[2]
                user_attempts[user]=user_attempts.get(user,0)+1
            except:
                pass
        elif "Success" in log:
            success +=1


    print("\n--- Log Summary ---")
    print("Failed attempts:", failed)
    print("Successful logins:", success)

    print("\n--- Attack Detection ---")
    for user,count in user_attempts.items():
        print(f"{user} → {count} failed attempts")

        if count >= 3:
            print(f"🚨 ALERT: Possible brute-force attack on {user}")



# Main Menu


def menu():
    print("\n=== Security Toolkit ===")
    print("1. Port Scanner + Service Detection")
    print("2. Brute-force Login")
    print("3. Log Analyzer")
    print("4. Exit")

while True:
    menu()
    choice = input("Select Option:")

    if choice == "1":
        port_scanner()
    elif choice == "2":
        brute_force()
    elif choice == "3":
        log_analyzer()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

    print("\nTask completed successfully!\n")

