import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:
    sockets_list = [sys.stdin, server]
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message.decode('utf-8'))
        else:
            sys.stdout.write("<Therapy Bot:> ")
            message = sys.stdin.readline()
            server.send(message.encode('utf-8'))
            sys.stdout.flush()
server.close()