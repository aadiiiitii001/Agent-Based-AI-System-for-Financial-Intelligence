# mcp_server/audit.py

import datetime

def log_action(agent_name: str, tool_name: str, payload: dict):
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "agent": agent_name,
        "tool": tool_name,
        "payload": payload
    }

    # For now, print — later store in DB
    print("AUDIT LOG:", log_entry)
