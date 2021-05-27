from os import pipe
import socket
import subprocess

BUFF_SIZE = 1024
HOST = "192.168.1.15"
PORT = 54545
FORMAT = "utf-8"
DISC_MSG = "!dc"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

def handle_client(conn, addr):
    print(f"[NEW CONN] {addr} connected.")

    while True:
        try:
            msg = conn.recv(BUFF_SIZE).decode(FORMAT)
            if len(msg)>0:
                print(f"[{addr[0]}]: {msg}")
                if msg.startswith("!") == True:
                    if msg == DISC_MSG:
                        print(f"[{addr[0]} DISCONNECTED]")
                        break
                    else:
                        command_handle(msg)
            else:
                break
        except ConnectionResetError:
            print(f"[{HOST}] --Nie odpowiada--")
            break        

def command_handle(comm):
    command = comm.lstrip("!").split(" ")
    try:
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        for x in p.stdout:
            conn.send(x)
    except:
        #conn.send(bytes(Exception), FORMAT)
        print("Blad w komendzie.")

sock.listen()
print(f"Listening on [{HOST}]")
while True:
    conn, addr = sock.accept()
    conn.send(b"Welcome!")
    handle_client(conn, addr)
