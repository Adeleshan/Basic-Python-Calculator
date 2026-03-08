def calculate(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator" 
    
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
b = input("Choose an operator (+, -, *, /): ")

if b in ["+", "-", "*", "/"]:
    print("You have chosen the operator: " + b)
    
    if b == "+":
        z = x + y
    elif b == "-":
        z = x - y
    elif b == "*":
        z = x * y
    elif b == "/":
        if y != 0:
            z = x / y
        else:
            z = "Error: Division by zero"
    
    print(f"Result: {z}")

else:
    print("Invalid operator. Please choose one of the following: +, -, *, /")
    for operator in ["+", "-", "*", "/"]:
        x_op = input("enter a valid operator: ") # Renamed to x_op so it doesn't overwrite your number 'x'
        if x_op == "+" or x_op == "-" or x_op == "*" or x_op == "/":
            # This calls the function and prints the result
            result = calculate(x, y, x_op)
            print(f"Result: {result}")
            break 
        else:
            break