from socket import *
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:

    sentence = input('Input sentence: ')

    clientSocket.send(sentence.encode('utf-8'))
    modifiedSentence = clientSocket.recv(1024)
    text = modifiedSentence.decode('utf-8')
    print("From Server:", text)

clientSocket.close()
