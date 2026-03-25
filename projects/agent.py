from ai_analyzer import analyze_with_ai

def security_agent(log_data):
    ai_result=analyze_with_ai(log_data)

    decision="Normal Activity"
    action="No action needed"

    if "attack" in ai_result.lower():
        decision ="Threat Dectect"
    if "brute" in ai_result.lower():
        action="Recommend: Block IP / Enable rate limiting"
    elif "mutli failed" in ai_result.lower():
        action ="Recommend : Lock account temporaily"

    return{
        "analysis" : ai_result,
        "decision" : decision,
        "action" : action
    }