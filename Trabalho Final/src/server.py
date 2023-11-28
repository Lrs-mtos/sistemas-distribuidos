import json
import socket
from dispatcher import Dispatcher
from skeleton import Skeleton
from servant import Servant

class UDPServer:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server_address)

        self.history = dict()
    def start(self):
        servant = Servant()
        skeleton = Skeleton(servant)
        dispatcher = Dispatcher(skeleton)

        while True:

            data, client_address = self.sock.recvfrom(4096)
            payload = json.loads(data.decode('utf-8'))
            request_id = payload['id']
            print(request_id)
            result = dispatcher.dispatch_request(json.dumps(payload))
            self.sock.sendto(json.dumps(result).encode('utf-8'), client_address)

if __name__ == '__main__':
    server_address = ('localhost', 8080)
    udp_server = UDPServer(server_address)
    udp_server.start()
