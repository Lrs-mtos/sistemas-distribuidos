#proxy.py

import json
import socket

class Proxy:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Definir o tempo limite em segundos
        self.sock.settimeout(2.0)
        # Criar um contador para gerar ids de requisição
        self.request_id = 0

    def invoke_method(self, method_name, *args):
        self.request_id += 1
        message = {
            "type": "request",
            "id": self.request_id,
            "obj_reference": "servant", 
            "method_id": method_name,
            "arguments": [json.dumps(arg) for arg in args]
        }

        payload = json.dumps(message).encode('utf-8')
        # Enviar a requisição para o servidor
        self.sock.sendto(payload, self.server_address)

        # Definir o número máximo de tentativas
        max_tries = 3

        # Iniciar o contador de tentativas
        tries = 0

        # Tentar receber a resposta do servidor
        while True:
            try:
                # Receber a resposta do servidor
                data, _ = self.sock.recvfrom(4096)
                # Decodificar a resposta
                result = json.loads(data.decode('utf-8'))
                # Sair do loop
                break
            except socket.timeout:
                # Incrementar o contador de tentativas
                tries += 1
                # Verificar se o número máximo de tentativas foi atingido
                if tries == max_tries:
                    # Lançar uma exceção
                    raise Exception("Servidor não respondeu após {} tentativas".format(max_tries))
                else:
                    # Retransmitir a requisição para o servidor
                    self.sock.sendto(payload, self.server_address)

        return result

    # Definir os mesmos métodos que o servant no proxy
    def eat(self, food, drink):
        return self.invoke_method("eat", food, drink)

    def play(self, game, join):
        return self.invoke_method("play", game, join)

    def sleep(self, hours, dream):
        return self.invoke_method("sleep", hours, dream)
