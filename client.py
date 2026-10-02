import socket
import os

#Messages
Disconnect_Message = "!Disconnected"
Turn_Message = "Your turn"
Wait_Message = "Wait, other player's turn"

#Colors of text in terminal
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[093m"
if os.name == "nt": os.system("") #Enables ANSI colors on terminal

#Create client socket and connect to server
Server_Addr = (socket.gethostbyname(socket.gethostname()), 5050)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Server_Addr)
print(f"{CYAN}{client.recv(2048).decode()}{RESET}") #which player am I?

#send messages to server
def send(msg):
    client.send(str.encode(msg))


def main():
    print(f"{GREEN}{client.recv(2048).decode()}{RESET}") #game has started
    run = True

    while run:
        myTurn = client.recv(2048).decode()
        print(f"{YELLOW}{myTurn}{RESET}")
        if myTurn == Turn_Message:
            send(input(f"{CYAN}Your move: {RESET}"))


main()