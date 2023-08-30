import socket
import operands

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1025  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:

        operation = operands.get_operands()
        if operation is None:
            s.close()
            break

        s.sendall(operation.encode("utf-8"))
        result = s.recv(1024)
        print(f"Result: {result.decode('utf-8')}")
    