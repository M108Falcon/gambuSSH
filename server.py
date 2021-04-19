import socket
import threading
import argparse

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


if __name__ == "__main__":

    """
    Initializing commandline arguments
    These arguments are purely optional and script can be run without them
    To see how to use them, type
    python3 server.py -h
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file" ,help="specify location for custom configuration file", required=False, default="")
    parser.add_argument("-p", "--port", help="specify PORT number", required=False, default = "")
    parser.add_argument("-m", "--maxconnections", help="specify max no of connections", required=False, default="")
    parser.add_argument("-4",help="Listen on IPv4", required=False, default="")
    parser.add_argument("-6", help="Listen on IPv6", required=False, default="")

    args = parser.parse_args()

    # set Port number
    PORT = 8000

    # set max no of connections
    MAXTHREADS = 100

    if args.port:
        PORT = int(args.port)
    if args.maxconnections:
        MAXTHREADS = int(args.maxconnections)

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

    print(f"[STARTING] Server is starting on PORT {PORT} with max {MAXTHREADS} connections allowed")
    startConneciton()
