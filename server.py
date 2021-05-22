#!/usr/bin/env python3

import argparse
import socket
import threading
from queue import Queue
from datetime import datetime
import time
import string
import random

def startConneciton():

    # removing data about previous connections in case of restart
    for c in all_connections: c.close()
    del all_connections[:]
    del all_addrs[:]

    # start socket
    global server
    try: 
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(SERVER, ADDR)

        # check for max connections
        if len(all_connections) < MAX_CONNECTIONS:
            server.listen()
            log_msg = f"Server listening on PORT {PORT} | started on {dt_string}"
            logging(log_msg)
            while True:
                conn, address = server.accept()
                server.setblocking(1) # prevents timeout

                # add connection info to lists
                all_connections.append(conn)
                all_addrs.append(address)
                log_msg = f"New connection | {address} connected"
                logging(log_msg)
        else:
            server.close()
            log_msg = f"Listener closed due to max limit of connections on {dt_string}"
            logging(log_msg)
    
    except socket.error as log_msg:
        logging(str(log_msg))
        

# recieve and send message to all connected clients
def handleClient(conns, addrs):

    # work only if there is a connection
    while(len(conns) > 0):
        # recieve all msgs and send the reply
        for c, a in conns, addrs:
            msg_length = c.recv(HEADER).decode(FORMAT)

            # check msg recieved and send reply
            if msg_length:
                msg_length = int(msg_length)
                msg = c.recv(msg_length).decode(FORMAT)

                # if disconnect msg is recieved, update list and close connection
                if msg == DISCONNECT_MESSAGE:
                    all_connections.remove(c)
                    all_addrs.remove(a)
                    c.close()
                    log_msg = f"{a} disconnected"
                    logging(log_msg)

                # call banner message generator for each client to send unique message to avoid pattern detection
                reply = sendReply(BANNER_LEN)

                # add delay to message
                time.sleep(DELAY)
                c.send(reply.encode(FORMAT))

            # if message not recieved, update list and close connection
            else:
                all_connections.remove(c)
                all_addrs.remove(a)
                c.close()
                log_msg = f"{a} disconnected"
                logging(log_msg)

# random banner alphanumeric message generator (each char has equal probability)
# default length = 32 chars
def sendReply(char_len):
    reply = "".join(random.choices(string.ascii_letters + string.digits, k=char_len))
    return reply

def logging(log_msg):
    with open('logs/gambuSSH.log', 'a') as writer:
        writer.writelines([log_msg, "\n"])


# create worker threads
def createWorkers():
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=work)
        thread.daemon = True
        thread.start()

# specigy jobs
def work():
    job = queue.get()
    if job == 1:
        startConneciton()
    if job == 2:
        handleClient(all_connections, all_addrs)

# create jobs and synchronize threads
def createJobs():
    for x in JOB_NUMBER:
        queue.put(x)
    
    queue.join()


if __name__ == "__main__":

    """
    Initializing commandline arguments
    These arguments are purely optional and script can be run without them
    To see how to use them, type
    python3 server.py -h
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="specify PORT number, default 8000 INT", required=False, default = "")
    parser.add_argument("-m", "--maxconnections", help="specify max no of connections, default 100 INT", required=False, default="")
    parser.add_argument("-d", "--delay", help="specify delay in sending msg in ms, default 2000 INT", required=False, default="")
    parser.add_argument("-b", "--bannerlength", help="specify reply banner, range: 3-255 INT", required=False, default="")
    parser.add_argument("-l", "--headerlength", help="change header length INT", required=False, default="")
    parser.add_argument("-4",help="Listen on IPv4", required=False, default="")
    parser.add_argument("-6", help="Listen on IPv6", required=False, default="")

    args = parser.parse_args()
    if args.port:
        PORT = int(args.port)
    if args.maxconnections:
        MAXTHREADS = int(args.maxconnections)
    if args.delay:
        DELAY = int(args.delay) % 1000
    if args.bannerlength:
        BANNER_LEN = int(args.bannerlength)
    if args.headerlength:
        HEADER = int(args.headerlength)

    # Server parameters
    PORT = 8000
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    HEADER = 4096

    # Thread sync data
    THREAD_COUNT = 2
    JOB_NUMBER = [1, 2]
    queue = Queue()
    MAX_CONNECTIONS = 100
    all_connections = []
    all_addrs = []

    # Message parameters
    DELAY = 2.000 # in miliseconds
    BANNER_LEN = 32
    DISCONNECT_MESSAGE = "!disconnect"
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")