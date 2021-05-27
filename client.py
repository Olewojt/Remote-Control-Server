#9A1C57C9

import socket
import subprocess
import threading
import os
import time 

#Functions
def clear_cs():
    os.system('cls')

def recv_msg():
    while True:
        try:
            recv_msg = client.recv(BUFF_SIZE)
            if len(recv_msg)>0:
                recv_msg = recv_msg.decode()
                print(recv_msg)
        except (ConnectionResetError, ConnectionAbortedError):
            print("\n Utracono polaczenie. Wpisz dowolny znak.")
            break

def send_msg():
    while True:
        try:
            send = input(f"[{HOST}]: ")
        except KeyboardInterrupt:
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            break
        if len(send)>0:
            if send == DISC_MSG:
                client.send(bytes(send, FORMAT))
                client.shutdown(socket.SHUT_RDWR)
                client.close()
                clear_cs()
                break
            client.send(bytes(send, FORMAT))
        
#Vars
BUFF_SIZE = 1024
HOST = "192.168.1.15"
PORT = 54545
FORMAT = "utf-8"
DISC_MSG = "!dc"

#Main 
while True:
    clear_cs()
    print("1.[STATUS]")
    print("2.[CONNECT]")
    print("3.[EXIT]")
    try:
        comm = input(": ")
    except KeyboardInterrupt:
        quit()
    if comm == '1':
        try:
            subprocess.check_call(["ping", "-n", "2", HOST], shell=True, stdout=subprocess.PIPE, timeout=2)
            print("[ALIVE]")
            time.sleep(2)
        except subprocess.TimeoutExpired as e:
            print("[DEAD]", e)
            time.sleep(2)
    elif comm == '2':
        clear_cs()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((HOST, PORT))

            #Creating thread
            X = threading.Thread(target=recv_msg)
            try:   #Prawdopodonie bezuzyteczne, jednak nie!
                X.start()
                send_msg()
            except (ConnectionAbortedError, ConnectionResetError):
                print("Zerwano polaczenie!")
        except ConnectionRefusedError:
            print("Odrzucono polaczenie [Serwer offline]?")
            time.sleep(2)
    elif comm == "3":
        quit()
         
       
