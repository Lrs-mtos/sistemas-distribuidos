def get_operands():
    """Get operands from user input."""
    operation = input("Enter operation or 'exit' to quit: ")
    if operation == "exit":
        return (None, None)
    return operation