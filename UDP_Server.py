#########################################################
# Description: This script generates a server provide
# a UDP connection to clients trying to send messages
# between each other by using UDP protocols.
# Author: Jose Neyra
#########################################################

# Import socket library
import socket
import time

# Connection address parameters
HOST = 'localhost'
PORT = 9454
port = 9555  # Additional port for sending data to client

# Socket object creation and set up for server
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.bind((HOST, PORT))


# File Functions
def writeFile(message):  # Function to write to mytextFile
    myFileWrite = open('mytextFile.txt', 'a')  # a to append new data
    newMessage = message[5:]  # Must ignore the WRITE part of the string
    myFileWrite.write(str(newMessage) + '\n')  # Write message to file
    myFileWrite.write(time.asctime(time.localtime(time.time())) + '\n')  # Write time to file
    myFileWrite.close()  # Close file
    return ('OKAY')


def readFile():  # Function to read file to client
    myFileRead = open('mytextFile.txt', 'r')  # r to read from file
    text = str(myFileRead.read())
    myFileRead.close()
    return (text)


def sendData(response, clientAddr):  # Function to send data
    data = response.encode()
    mySocket.sendto(data, clientAddr)


print('Ready to receive')
stopping = False

# Loop
while not stopping:  # Loop until user stops

    message, clientAddr = mySocket.recvfrom(1024)
    print(message)

    if 'WRITE' in str(message):
        response = str(writeFile(message))
        sendData(response, clientAddr)

    elif 'GET' in str(message):
        response = str(readFile())
        sendData(response, clientAddr)

    elif 'stop' in str(message):
        sendData('Program stopped', clientAddr)
        stopping = True

    else:
        response = 'ERROR:Please enter WRITE, GET, or stop at the beginning of message'
        sendData(response, clientAddr)

    time.sleep(1)
