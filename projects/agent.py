from ai_analyzer import analyze_with_ai
from scanner import port_scanner

memory=[]

def security_agent(log_data):
    global memory
    # print("AI INput",log_data)
    ai_result=analyze_with_ai(log_data)

    decision="Normal Activity"
    action="No action needed"

    tool_output=[]

    target_user=list(log_data["users"].keys())[0] if log_data["users"] else "unknown"

    # if "attack" in ai_result.lower():
    #     decision ="Threat Dectect"
    if "brute" in ai_result.lower() or "failed login" in ai_result.lower():
        action="Running port scan on target ...."
        memory.append(target_user)
        target = "127.0.0.1",
        tool_output=port_scanner(target)
    

    return{
        "analysis" : ai_result,
        "decision" : decision,
        "action" : action,
        "memory":memory,
        "tool_output":tool_output
    }