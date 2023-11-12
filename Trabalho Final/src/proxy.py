import json
import socket

class Proxy:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def invoke_method(self, method_name, *args):
        message = {
            "type": "request",
            "id": 1,
            "obj_reference": "servant", 
            "method_id": method_name,
            "arguments": [json.dumps(arg) for arg in args]
        }

        payload = json.dumps(message).encode('utf-8')
        self.sock.sendto(payload, self.server_address)
        data, _ = self.sock.recvfrom(4096)
        return json.loads(data.decode('utf-8'))
