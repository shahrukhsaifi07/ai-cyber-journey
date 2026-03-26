def decide_response(detection_result):
    if detection_result["threat"]:
        return {
            "action":"block_and_scan",
            "message":"Threat detected. Taking action."
        }
    return {
        "action":"none",
        "message":"System normal"
    }