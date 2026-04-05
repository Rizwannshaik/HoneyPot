import socket
import threading

from file_system import read_file, list_files
from Detector import detect_attack
from Logger import log_event

HOST = "0.0.0.0"
PORT = 2222

def handle_client(client, addr):
    ip = addr[0]

    print(f"[+] {ip} connected")

    client.send(b"login: ")
    username = client.recv(1024).decode().strip()

    client.send(b"password: ")
    password = client.recv(1024).decode().strip()

    log_event({
        "ip": ip,
        "username": username,
        "password": password,
        "event": "login_attempt"
    })

    client.send(b"\nWelcome to Ubuntu 20.04 LTS\n$ ")

    while True:
        command = client.recv(1024).decode().strip()

        if command == "":
            break

        # Log command
        log_event({
            "ip": ip,
            "username": username,
            "command": command,
            "event": "command"
        })

        # Detect attacks
        alerts = detect_attack(command)
        for alert in alerts:
            print(f"[ALERT] {ip}: {alert}")
            log_event({
                "ip": ip,
                "alert": alert,
                "event": "alert"
            })

        # Fake filesystem
        if command == "ls":
            response = list_files()

        elif command.startswith("cat "):
            path = command.split(" ", 1)[1]
            response = read_file(path)

            if "passwd" in path or "bank_details" in path:
                log_event({
                    "ip": ip,
                    "file": path,
                    "event": "file_access_trap"
                })

        elif command == "exit":
            break

        else:
            response = "command not found"

        client.send((response + "\n$ ").encode())

    client.close()
    print(f"[-] {ip} disconnected")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(100)

    print(f"[🔥] Honeypot running on port {PORT}")

    while True:
        client, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()


if __name__ == "__main__":
    start_server()