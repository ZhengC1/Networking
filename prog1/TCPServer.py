#!/usr/local/bin/python
"""
Author: Chun Zheng 
Language: Python 3.4.1
Class: Networking 4450
"""

from socket import * 
"""I imported multiprocessing and hope to use the Proces 
 so that i may just put it in a subprocess
 this took me sooooooooooooooo long Dr. Norris.  
"""
from multiprocessing import Process
import time

serverPort = 15020 
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)
print("The Server is ready to recieve")
#i put all the entire server call or execution in a 
#function so i can thread it in a queue

def connection(connectionSocket):
    sentence = ''
"""this while loop will keep looking for the 'quit' keyword so that
 it can close the socket after
"""
    while sentence != 'quit': 
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)
#socket closes when while loop is done. 
    connectionSocket.close()
#this calls the connection function
""" I have this while true so that i can multiThread
and push the process to a sub process 
"""
while True: 
    connectionSocket, addr = serverSocket.accept()
    p = Process(target=connection, args=(connectionSocket,))
    p.start()


