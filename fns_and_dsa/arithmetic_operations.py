def perform_operation(num1: float, num2: float, operation: str):
    if operation in 'add':
        return num1 + num2
    elif operation in 'subtract':
        return num1 - num2
    elif operation in 'multiply' :
        return num1 * num2
    elif operation in 'divide':
        if num2 == 0:
            return "Error: Division by zero is undefined."
        return num1 / num2
    else:
        return "Error: Unsupported operation."
