

def perform_operation(num1, num2, operation):

    # operation = input("Enter operation (+, -, *, /): ")
    # num1 = float(input("Enter first number: "))
    # num2 = float(input("Enter second number: "))

    if operation == 'add':
        result = num1 + num2
        return result
    elif operation == 'subtract':
        result = num1 - num2
        return result
    elif operation == 'multiply':
        result = num1 * num2
        return result
    elif operation == 'divide':
       if num2 == 0 or num1 == 0:
            print("Error:Cannot divide by zero")  
       else:
            result = num1 / num2
    else:
        result =  "Error: Invalid operation."
        return result

