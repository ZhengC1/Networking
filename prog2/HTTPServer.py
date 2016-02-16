#!/usr/local/bin/python

#these are the imports that I needed
import threading
import string
import os
import mimetypes
import codecs

from socket import *

def worker(connectionSocket):
    try:
        #start recieving
        sentence = connectionSocket.recv(1024)
        #decode the request
        request = sentence.decode()

        #gets the point of HTTP or the point after the url
        index = request.find('HTTP/1.1\r\nHost:') - 1

        #checks for a GET request
        if request[:3:] != 'GET':
            #file directory to send error
            send_file = os.getcwd() + "/400errorDoc.html"
            error = open(send_file, "rb")
            error_read = error.read()
            connectionSocket.send(error_read)
        directing = os.getcwd()
        directory = directing + request[4:index:]
        open_file = open(directory, "rb")
        send_file = open_file.read()
        #there doesnt seem to be a different from sendall and send?
        connectionSocket.sendall(send_file)
        connectionSocket.close()

    #if all else fails, that means theres no file so i send the 404
    except FileNotFoundError:
        no_file = os.getcwd() + "/404errorDoc.html"
        no_file_open = open(no_file, "rb") 
        send_no_file = no_file_open.read() 
        connectionSocket.send(send_no_file)
        connectionSocket.close()

serverPort = 15020
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((gethostname(), serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while 1:
    (connectionSocket, addr) = serverSocket.accept()
    t = threading.Thread(target = worker, args=(connectionSocket, ))
    t.start() 
