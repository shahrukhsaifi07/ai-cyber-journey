def analyze_logs():
    try:
        with open("logs.txt", "r") as file:
            logs = file.readlines()
    except:
        print("logs.txt not found!")
        return
    # print(logs)
    failed = 0
    success = 0
    user_attempts = {}
    users={}
    ips={}

    for log in logs:
        log=log.strip()
        # log_lower = log.lower()

        if "FAILED" in log:
            failed += 1

            # try:
               
            # except:
            #     pass

        elif "SUCCESS" in log:
            success += 1
        
        if "user=" in log:
             user = log.split("user=")[1].split()[0]
             users[user] = users.get(user, 0) + 1

        if "ip=" in log:
            ip=log.split("ip=")[1]
            ips[ip]=ips.get(ip,0)+1

    result={
        "failed":failed,
        "success":success,
        "users":users,
        "ips":ips
    }
    return result
    # print("\n--- Log Summary ---")
    # print("Failed attempts:", failed)
    # print("Successful logins:", success)

    # print("\n--- Attack Detection ---")
    # for user, count in user_attempts.items():
    #     print(f"{user} → {count} failed attempts")

    #     if count >= 3:
    #         print(f" ALERT: Possible brute-force attack on {user}")