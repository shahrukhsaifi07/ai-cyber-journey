def analyze_logs():
    try:
        with open("logs.txt", "r") as file:
            logs = file.readlines()
    except:
        print("logs.txt not found!")
        return

    failed = 0
    success = 0
    user_attempts = {}

    for log in logs:
        if "Failed" in log:
            failed += 1

            try:
                user = log.split()[2]
                user_attempts[user] = user_attempts.get(user, 0) + 1
            except:
                pass

        elif "Success" in log:
            success += 1


    result={
        "failed":failed,
        "success":success,
        "users":user_attempts
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