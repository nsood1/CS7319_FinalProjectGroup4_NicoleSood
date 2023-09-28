import socket
import select
import sys

from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port = int(sys.argv[2])

"""
binds the server to an entered IP address and at the
specified port number.
The client must be aware of these parameters
"""
server.bind((IP_address, Port))

"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
server.listen(100)

list_of_clients = []


def clientthread(conn, addr, clients):
    conn.send("Welcome to this therary session".encode('utf-8'))

    while True:
        try:
            message = conn.recv(2048)
            if message:
                # Print the received message
                print("<" + addr[0] + "> " + message.decode('utf-8'))

                # Process the message and send a response
                response = "You said: " + message.decode('utf-8')
                conn.send(response.encode('utf-8'))

                message = sys.stdin.readline()
                conn.send(message.encode('utf-8'))
                sys.stdout.write("<TherapyBot>")
                sys.stdout.write(message)
                sys.stdout.flush()

            else:
                # If the message is empty, remove the connection
                remove(conn)

        except:
            continue



"""Using the below function, we broadcast the message to all
clients whose object is not the same as the one sending
the message """


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode('utf-8'))
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)


"""The following function simply removes the object
from the list that was created at the beginning of
the program"""


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + " connected")
    start_new_thread(clientthread, (conn, addr, list_of_clients))

conn.close()
server.close()
