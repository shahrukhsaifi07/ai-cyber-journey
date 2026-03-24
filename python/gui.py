import tkinter as tk
import port_scanner
def run_scanner():
    print("Running scanner")
    port_scanner()

def run_bruteforce():
    print("Running brute force...")

def run_logs():
    print("Running log analyzer...")

root = tk.Tk()
root.title("Security Toolkit")
root.geometry("400x300")
tk.Button(root,text="Scan Ports", command=run_scanner).pack(pady=10)
tk.Button(root,text="Brute Force", command=run_scanner).pack(pady=10)
tk.Button(root,text="Log Analyzer", command=run_scanner).pack(pady=10)

root.mainloop()