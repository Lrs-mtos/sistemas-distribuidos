import socket
import threading
import calc
import temp_converter

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 1024  # Port to listen on (non-privileged ports are > 1023)

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

def perform_operation(operation, operands, functions):
                if operation in functions:
                    result = functions[operation](*operands)
                    return str(result).encode("utf-8")
                else:
                    return None
                

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

            response = perform_operation(operation, operands, operations) or perform_operation(operation, operands, temperatures)
            if response is None:
                raise ValueError()
            else: 
                print(f"Sending {response.decode('utf-8')!r}")
                conn.sendall(response)

        except (ValueError, IndexError, ZeroDivisionError):
            conn.sendall("Operation not supported by this server. \nType '--h' or 'help' to see the available commands\n".encode("utf-8"))

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