from socket import *
serverName = 'localhost'
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print('Connected to server')
while True:

    sentence = input()

    clientSocket.send(sentence.encode('utf-8'))
    text = clientSocket.recv(1024).decode('utf-8')
    print("                         <<< From Server:", text)

clientSocket.close()
