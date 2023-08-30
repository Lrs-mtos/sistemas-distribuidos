def get_operands():
    """Get operands/temperature from user input."""
    operation = input("Enter operation/temperature or 'exit' to quit: ")
    if operation == "exit":
        return (None)
    return operation