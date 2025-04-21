import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)                                 # this sends a message right away

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)

    # Preparing the first message with the length of the actual data
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))       # pad the first message to 64 bytes as per the agreed protocol
    client.send(send_length)
    client.send(message)
    print (client.recv(2048).decode(FORMAT))

send("Hello!")
input()
send("Hello everyone!")
input()
send("Hello every two!")
input()
send("Hello every 3!")
input()
send("Hello every Four!")
input()
send(DISCONNECT_MESSAGE)
