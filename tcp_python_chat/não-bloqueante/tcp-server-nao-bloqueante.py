import time
from socket import *
import threading

def handle_client(clientSocket):
    while 1:
        sentence = clientSocket.recv(1024)
        text = sentence.decode('utf-8')
        print("From Client:", text)
        if text == 'exit':
            break
        capitalizedSentence = text.upper()
        clientSocket.send(capitalizedSentence.encode('utf-8'))
    clientSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()

# Crie uma nova thread para lidar com o cliente
client_handler = threading.Thread(target=handle_client, args=(connectionSocket,))
client_handler.start()
