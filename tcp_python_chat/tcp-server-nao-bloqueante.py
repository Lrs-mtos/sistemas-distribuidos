import socket
import select

# Configurações do servidor
HOST = ''
PORT = 12000

# Criação do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Define o número máximo de conexões em espera

print(f"Servidor ouvindo em {HOST}:{PORT}")

# Lista de sockets para seleção (leitura)
sockets_list = [server_socket]

while True:
    # Usa select para monitorar os sockets para leitura, escrita e erro
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for sock in read_sockets:
        if sock == server_socket:
            # Novo cliente se conectou
            client_socket, client_address = server_socket.accept()
            sockets_list.append(client_socket)
            print(f"Cliente conectado: {client_address}")

            # Envia uma mensagem de boas-vindas
            client_socket.send("Bem-vindo ao servidor!".encode())
        else:
            # Um cliente existente enviou uma mensagem
            try:
                message = sock.recv(1024).decode()
                if message:
                    print(f"Recebido: {message}")

                    # Broadcast da mensagem para todos os clientes (exceto o remetente)
                    for socket_item in sockets_list:
                        if socket_item != server_socket and socket_item != sock:
                            try:
                                socket_item.send(message.encode())
                            except:
                                # Remove o socket se a conexão estiver quebrada
                                socket_item.close()
                                sockets_list.remove(socket_item)
            except:
                # Remove o socket se ocorrer um erro
                sock.close()
                sockets_list.remove(sock)
                continue
