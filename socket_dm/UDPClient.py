from socket import *

serverName = '127.0.0.1'
serverPort = 12000


clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('A:')

    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print('B:', modifiedMessage.decode())

clientSocket.close()


