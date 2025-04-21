import socket
import threading

HEADER = 64
PORT =  5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print (f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # recv() blocks for incoming data, 
                                                      # HEADER is the number of bytes to accept
                                                      # this depends on the protocol to specify the first message
                                                      # Suppose the first message would say how long are subsequent messages

        if msg_length:                                # this is to avoid parsing errors because of the first None connection message
            msg_length = int(msg_length)                  
            msg = conn.recv(msg_length).decode(FORMAT)    # now recv() for the expected message length
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))

    print ("[CLOSING} connection")
    conn.close()

def start_server():
    server.listen()
    print (f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()         # accept() blocks for incoming connections

        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()                       # a thread thus gets created upon each client connection
        print (f"[ACTIVE CONNECTIONS] {str(threading.active_count() - 1)}")  # activeCount includes the server process itself

if __name__ ==  "__main__":
    print ("[STARTING] Server is starting...")
    start_server()


#TODO
# send messages from one client to another
# send non-string messages - json serialised or pickle serialised
# constant ping by clients
# send from another PC on same network
# send from another PC on different network e.g the internet
