import socket
import threading

# set Port number
PORT = 8000

# get local machine address
SERVER = socket.gethostbyname(socket.gethostname())

# store info in tuple for network socket
ADDR = (SERVER, PORT)

# format
FORMAT = 'utf-8'

# Connection Header of 64bytes
HEADER = 64

# disconnection message
DISCONNECT_MESSAGE = "!disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handleClient(conn, address):
    print(f"[NEW CONNECTION] {address} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{address}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()


def startConneciton():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        thread.join()


print(f"[STARTING] Server is starting on PORT {PORT}")
startConneciton()
