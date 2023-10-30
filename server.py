import socket
import sys
from main import *
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(100)
list_of_clients = []
# def clientthread(conn, addr, clients):
#     conn.send("Welcome to this therapy session".encode('utf-8'))
#     chatbot = initialize_chatbot("database.txt")
#     while True:
#         try:
#             message = conn.recv(2048)
#             if message:
#                 print("<" + addr[0] + "> " + message.decode('utf-8'))
#                 response = chatbot.respond(message.decode('utf-8'))
#                 if is_response_empty(response):
#                     conn.send('I am sorry, I did not get that'.encode('utf-8'))
#                 else:
#                     conn.send(response.encode('utf-8'))
#             else:
#                 remove(conn)
#
#         except:
#             continue

def clientthread(conn, addr, clients):
    conn.send("Welcome to this therapy session".encode('utf-8'))
    chatbot = initialize_chatbot("database.txt")

    while True:
        try:
            message = conn.recv(2048)
            if message:
                print("<" + addr[0] + "> " + message.decode('utf-8'))
                response = chatbot.respond(message.decode('utf-8'))
                print(response)
                if response == None:
                    conn.send("Sorry, I didn't understand".encode('utf-8'))
                else:
                    conn.send(response.encode('utf-8'))
            else:
                remove(conn)
        except Exception as e:
            print("Error:", e)
            continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode('utf-8'))
            except:
                clients.close()
                remove(clients)

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
