import socket

# Set Port number
PORT = 8000

# Connection Header of 64bytes
HEADER = 64

# format
FORMAT = 'utf-8'

# Connect to server
SERVER = "192.168.1.25"

# Store the info in the tuple for network socket
ADDR = (SERVER, PORT)

# disconnection message
DISCONNECT_MESSAGE = "!disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def sendMessage(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

sendMessage("yo boi")
input()
sendMessage("yo bois")
input()
sendMessage(DISCONNECT_MESSAGE)
