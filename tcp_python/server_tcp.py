import socket
import threading
import calc

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 1024  # Port to listen on (non-privileged ports are > 1023)


def handle_client(conn, addr):
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        data = data.decode("utf-8")
        print(f"Received {data!r}")

        try:
            parts = data.split()
            operation = parts[0]
            operands = [int(operand) for operand in parts[1:]]

            operations = {
                "add": calc.add,
                "sub": calc.sub,
                "mul": calc.mul,
                "div": calc.div,
            }

            if operation in operations:
                result = operations[operation](*operands)
                response = str(result).encode("utf-8")
                print(f"Sending {result!r}")
                conn.sendall(response)
            else:
                conn.sendall("Invalid operation".encode("utf-8"))

        except (ValueError, IndexError, ZeroDivisionError):
            conn.sendall("Invalid input".encode("utf-8"))

    print(f"Connection closed for {addr}.")
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for connection...")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()