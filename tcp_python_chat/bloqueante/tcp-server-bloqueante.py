from socket import *
import threading

def receive_message(sock):
    while True:
        message = sock.recv(1024)
        if not message:
               break
        print("From Client:", message.decode('utf-8'))


serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("##################################")
print("# The server is ready to receive #")
print("##################################")

connectionSocket, addr = serverSocket.accept()

#Thread para receber mensagens do cliente
receive_thread = threading.Thread(target=receive_message, args=(connectionSocket,))
receive_thread.start()

while 1:
     sentence = input('From client:')
     connectionSocket.send(sentence.encode('utf-8'))

connectionSocket.close()
