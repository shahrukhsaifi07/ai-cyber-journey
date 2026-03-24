from scanner import port_scanner
from brute_force import brute_force
from log_analyzer import log_analyzer

def menu():
    print("\n=== Security Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute-force Login")
    print("3. Log Analyzer")
    print("4. Exit")

while True:
    menu()
    choice = input("Select option: ")

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