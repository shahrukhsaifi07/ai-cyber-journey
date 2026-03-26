def detect_threat(log_data):
    if log_data["failed"] > 3:
        return {
            "threat" :True,
            "type":"Brute Force",
            "target_ip":max(log_data["ips"],key=log_data["ips"].get)
        }
    return {"threat":False}