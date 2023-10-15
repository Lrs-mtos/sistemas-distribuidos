import time
from socket import *
import threading

def handle_client(clientSocket):
    while 1:
        sentence = clientSocket.recv(1024)
        text = sentence.decode('utf-8')
        print("From Client:", text)
        if text == '':
            break
        server_sentence = input('Input:')
        clientSocket.send(server_sentence.encode('utf-8'))
    clientSocket.close()


def handle_connection():
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    client_handler = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_handler.start()

connection_handle = threading.Thread(target=handle_connection)
connection_handle.start()
# Crie uma nova thread para lidar com o cliente

