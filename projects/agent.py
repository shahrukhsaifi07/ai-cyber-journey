from ai_analyzer import analyze_with_ai
from scanner import port_scanner
from blocker import block_ip
from detection_agent import detect_threat
from response_agent import decide_response
from action_agent import execute_action
memory=[]

def security_agent(log_data):
    global memory
    # print("AI INput",log_data)
    try:

        ai_result=analyze_with_ai(log_data)
    except:
        ai_result="AI analysis failed, using system detection"

    print(ai_result)

    detecion=detect_threat(log_data)
    response=decide_response(detecion)
    decision= analyze_with_ai(log_data)
    results=[]
    if decision =="block_ip":
        results.append(block_ip(target_ip))
    elif decision == "scan_ports":
        results.extend(port_scanner(target_ip))

    action="No action needed"

    tool_output=[]


    target_user=list(log_data["users"].keys())[0] if log_data["users"] else "unknown"
    target_ip = max(log_data["ips"], key=log_data["ips"].get) if log_data["ips"] else None
    print("TARGET IP:", target_ip)

    if detecion["threat"]:
        target_ip = detecion["target_ip"]
        tool_output=execute_action(response,target_ip)
    else:
        target_ip = None
    # if "attack" in ai_result.lower(): or "failed login" in ai_result.lower()
    #     decision ="Threat Dectect" "brute" in ai_result.lower()
    if log_data["failed"] > 3:
        decision=f"Brute Force Attack from {target_ip}"

        action="Running port scan on target ...."
        memory.append(target_user)
        # target = "127.0.0.1",
       
        tool_output=port_scanner(target_ip)
        block_result=block_ip(target_ip)
        tool_output.append(block_result)
        ai_result +="\n\n[Sytem]:Brute force attack confirmed"

    return{
        "analysis" : ai_result,
        "decision" : decision,
        "action" : action,
        "detection":detecion,
        "response":response,
        "memory":memory,
        "target_ip":target_ip,
        "tool_output":tool_output
    }