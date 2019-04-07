#########################################################
# Description: This script generates a client interface
# to connect to the server to be able to chat with other
# users by specifying their IP address and internet
# port. This network uses UDP protocols.
# Author: Jose Neyra
#########################################################

# Import Socket Library
import socket

# Sets up connection address parameters
HOST = 'localhost'
PORT = 9454

# Create and set socket object for client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('By Jose Neyra, Computer Networks, UDP CHAT ROOM:\n')
print('RULES: Input "WRITE" then your message to write to chat,\n"GET" to read the chat,\nand "stop" to stop:\n')
print('*************************************************************')
message = 'Go'

while message != ('stop' or ' '):  # Loop until user stops

    message = input('Enter your message: ')

    data = str.encode(message)  # Send data to server, must encode first
    s.sendto(data, (HOST, PORT))

    response = ' '  # Set up while loop until a response from server is given
    while response is ' ':
        response, address = s.recvfrom(2048)

    print(str(response))  # Print response from server
