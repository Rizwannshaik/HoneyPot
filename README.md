# HoneyPot
Advanced multi-threaded honeypot system built in Python to simulate a vulnerable server, capture real attacker behavior, perform GeoIP tracking, detect malicious patterns, and deploy deception techniques using a fake filesystem.

# 🛡️ Advanced Honeypot System (Cybersecurity Project)

A production-ready, multi-threaded honeypot designed to simulate a vulnerable Linux server and capture real-world attacker activity.

This project demonstrates both **offensive understanding** and **defensive security engineering** by logging intrusion attempts, analyzing attacker behavior, and implementing deception techniques.

---

## 🚀 Key Features

- ⚡ Multi-threaded server (handles multiple attackers simultaneously)
- 🌍 GeoIP tracking (attacker country, city, coordinates)
- 🔐 Credential harvesting (username/password logging)
- 💻 Command monitoring (full attacker interaction logging)
- 🧠 Attack pattern detection (flags suspicious activity)
- 🪤 Fake file system trap (detects sensitive file access attempts)
- 📊 JSON logging (ready for dashboards & SIEM integration)

---

## 🧱 Architecture

Attacker → Honeypot Server → Logger → Detection Engine → GeoIP Enrichment → Logs

---

## 🛠️ Tech Stack

- Python (Socket Programming, Threading)
- GeoIP Database (GeoLite2)
- JSON (Structured logging)
- Custom Detection Engine

---

---

## ⚙️ How It Works

1. Attacker connects to the honeypot
2. Fake login prompt captures credentials
3. Commands are logged and analyzed
4. Suspicious patterns trigger alerts
5. Fake filesystem traps sensitive access attempts
6. GeoIP enriches attacker location data
7. All events are stored in structured logs

---

## 🧪 Example Attack Log

```json
{
  "ip": "45.33.32.1",
  "geo": {
    "country": "United States",
    "city": "Newark"
  },
  "username": "root",
  "password": "admin",
  "command": "cat /etc/passwd",
  "event": "file_access_trap"
}
