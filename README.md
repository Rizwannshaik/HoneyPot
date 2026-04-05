                                            --  HoneyPot  -- 
Advanced multi-threaded honeypot system built in Python to simulate a vulnerable server, capture real attacker behavior, detect malicious patterns, and deploy deception techniques using a fake filesystem.

# 🛡️ Advanced Honeypot System (Cybersecurity Project)

A production-ready, multi-threaded honeypot designed to simulate a vulnerable Linux server and capture real-world attacker activity.

This project demonstrates both **offensive understanding** and **defensive security engineering** by logging intrusion attempts, analyzing attacker behavior, and implementing deception techniques.

---

## 🚀 Key Features

- ⚡ Multi-threaded server (handles multiple attackers simultaneously)
- 🔐 Credential harvesting (username/password logging)
- 💻 Command monitoring (full attacker interaction logging)
- 🧠 Attack pattern detection (flags suspicious activity)
- 🪤 Fake file system trap (detects sensitive file access attempts)
- 📊 JSON logging (ready for dashboards & SIEM integration)

---

🧱 Architecture

Attacker → Honeypot Server → Logger → Detection Engine → Logs

🛠️ Tech Stack
Python (Socket Programming, Threading)
JSON Logging
Custom Detection Engine

---


📂 Project Structure

honeypot.py → Main server
fake_fs.py → Fake file system
detector.py → Attack detection
logger.py → Logging engine

---

## ⚙️ How to Run
python3 honeypot.py

Test using:

nc localhost 2222

---

## ⚙️ How It Works

1. Attacker connects to the honeypot
2. Fake login prompt captures credentials
3. Commands are logged and analyzed
4. Suspicious patterns trigger alerts
5. Fake filesystem traps sensitive access attempts
6. All events are stored in structured logs

---

## 🧪 Example Attack Log

```json
    {
        "ip": "127.0.0.1",
        "username": "root",
        "password": "123456",
        "event": "login_attempt",
        "timestamp": "2026-04-05T15:16:41.363628"
    },
    {
        "ip": "127.0.0.1",
        "username": "root",
        "command": "ls",
        "event": "command",
        "timestamp": "2026-04-05T15:16:42.674517"
    },
    {
        "ip": "127.0.0.1",
        "username": "root",
        "command": "cat /etc/passwd",
        "event": "command",
        "timestamp": "2026-04-05T15:16:56.491689"
    },
    {
        "ip": "127.0.0.1",
        "file": "/etc/passwd",
        "event": "file_access_trap",
        "timestamp": "2026-04-05T15:16:56.493708"
    },
    {
        "ip": "127.0.0.1",
        "username": "root",
        "command": "wget malware.sh",
        "event": "command",
        "timestamp": "2026-04-05T15:17:10.524848"
    },
    {
        "ip": "127.0.0.1",
        "alert": "Suspicious command detected: wget",
        "event": "alert",
        "timestamp": "2026-04-05T15:17:10.526358"
    },
    {
        "ip": "127.0.0.1",
        "username": "root",
        "command": "ls",
        "event": "command",
        "timestamp": "2026-04-05T15:17:16.386600"
    }

