from scanner import port_scanner
from blocker import block_ip

def execute_action(response,target_ip):
    result=[]

    if response["action"]=="block_and_scan":
        result.extend(port_scanner(target_ip))
        result.append(block_ip(target_ip))

    return result