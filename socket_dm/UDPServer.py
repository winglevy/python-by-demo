from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive!")

while True:
    messages, clientAddress = serverSocket.recvfrom(2048)

    print('A:', messages.decode())

    modifiedMessage = input('B:')
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)