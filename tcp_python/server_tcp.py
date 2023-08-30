import socket
import threading
import calc
import temp_converter

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 1025  # Port to listen on (non-privileged ports are > 1023)


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

            temperatures = {
                "c2k": temp_converter.celsius2kelvin,
                "k2c": temp_converter.kelvin2celsius,
                "k2f": temp_converter.kelvin2fahrenheit,
                "f2k": temp_converter.fahrenheit2kelvin,
                "c2f": temp_converter.celcius2fahrenheit,
                "f2c": temp_converter.fahrenheit2celcius,
            }

            if operation in temperatures:
                result = temperatures[operation](*operands)
                response = str(result).encode("utf-8")
                print(f"Sending {result!r}")
                conn.sendall(response)

            elif operation in operations:
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