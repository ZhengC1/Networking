#!/usr/local/bin/python

from click import echo
from socket import *
from multiprocessing import Process
import time

server_port = 15020
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('',server_port))

server_socket.listen(1)
echo("The Server is ready to recieve")

def connection(connection_socket):
    recieved_data = ''
    while  recieved_data != 'quit':
        received_data = connection_socket.recv(1024)
        connection_socket.send(recieved_data.upper())
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    p = Process(target=connection, args=(connectionSocket,))
    p.start()


