#!/usr/local/bin/python
"""
Author: Chun Zheng and ROSS | Kurose
Language: Python 3.4.1
Class: Networking 4450
"""

#Author: Chun Zheng and Kurose | Ross
#Language: Python 3.4.1

from socket import *
#this is the Student server
serverName = "student.cs.appstate.edu"
#this it da port number assigned by my prof
serverPort = 15020
#This to me just means its TCP woo!
clientSocket = socket(AF_INET, SOCK_STREAM)
#connecting via the server and serverport
clientSocket.connect((serverName,serverPort))
sentence = 0
while sentence != 'quit':
#changed it from raw_input and takes from the cmd line
    sentence = input('Input:')
# i added encode on the sentence so it could sent it as bytes over the connection
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
# here i decode using the client, i feel like i could have done so
# with the server...but i didnt.
    print ("From Server:" , modifiedSentence.decode())

#this is finally executed after the while loop is finished.
clientSocket.close()
