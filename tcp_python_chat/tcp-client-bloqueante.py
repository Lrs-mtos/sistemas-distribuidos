""" 
O que teve que ser mudado no código do cliente, considerando o código original,
foi o loop inserido para que el possa enviar várias mensagens ao servidor.
Além disso, o cliente também pode receber mensagens do servidor. Como o cliente
já tinha sido feito tanto para enviar quanto para receber mensagens, não houve
muita mudança no código.
"""


from socket import *
serverName = 'localhost'
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:

    sentence = input('Input sentence:')

    clientSocket.send(sentence.encode('utf-8'))
    modifiedSentence = clientSocket.recv(1024)
    text = modifiedSentence.decode('utf-8')
    print("From Server:", text)
    clientSocket.close()
