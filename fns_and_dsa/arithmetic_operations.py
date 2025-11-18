

def perform_operation(num1, num2, operation):
    """Performs a basic arithmetic operation based on user input."""
    # operation = input("Enter operation (+, -, *, /): ")
    # num1 = float(input("Enter first number: "))
    # num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
        return result
    elif operation == '-':
        result = num1 - num2
        return result
    elif operation == '*':
        result = num1 * num2
        return result
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            return result
        else:
            return "Error: Division by zero is not allowed."
    else:
        result =  "Error: Invalid operation."
        return result

# if __name__ == "__main__":