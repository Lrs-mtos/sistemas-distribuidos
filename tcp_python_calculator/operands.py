#consertar o envio do help para o servidor
def get_operands():
    
    operation = input("Enter operation or 'exit' to quit: ")
    if operation == "--h" or operation == "help":
        print("Available operations: add [opr1 opr2]\n, sub [opr1 opr2]\n, mul [opr1 opr2]\n, div [opr1 opr2]\n, c2k [value]\n, k2c [value]\n, k2f [value]\n, f2k [value]\n, c2f [value]\n, f2c [value]\n")
    if operation == "exit":
        return (None)
    return operation


