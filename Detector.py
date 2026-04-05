suspicious_commands = [
    "rm -rf",
    "wget",
    "curl",
    "nc",
    "nmap",
    "bash -i",
    "chmod 777",
]

def detect_attack(command):
    alerts = []

    for pattern in suspicious_commands:
        if pattern in command:
            alerts.append(f"Suspicious command detected: {pattern}")

    if "root" in command:
        alerts.append("Privilege escalation attempt")

    return alerts