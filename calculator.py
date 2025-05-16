import sys

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == '+':
    result = num1 + num2
elif operation == '-': 
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation. Please use +, -, *, or /."

if len(sys.argv) != 4:
    print("Error: Please provide arguments in the format of: num1 operation num 2")

print(result)
