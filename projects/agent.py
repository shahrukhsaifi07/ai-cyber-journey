from ai_analyzer import analyze_with_ai
from scanner import port_scanner

def security_agent(log_data):
    ai_result=analyze_with_ai(log_data)

    decision="Normal Activity"
    action="No action needed"

    tool_output=[]

    if "attack" in ai_result.lower():
        decision ="Threat Dectect"
    if "brute" in ai_result.lower() or "failed login" in ai_result.lower():
        action="Running port scan on target ...."
        target = "127.0.0.1"
        tool_output=port_scanner(target)
    

    return{
        "analysis" : ai_result,
        "decision" : decision,
        "action" : action,
        "tool_output":tool_output
    }