def block_ip(ip):
    try:
        with open("blocked_ips","r") as f:
            if ip in f.read():
                return f"IP {ip} already blocked"
    except:
        pass

    with open("blocked_ips.txt","a") as f:
        f.write(ip + "\n")

    return f"IP {ip} blocked successfull"