# This prompts the user to enter the first number
first_number = input("Enter the first number: ")

# This converts the first number from string to float
first_number = float(first_number)

# This prompts the user to enter the second number
second_number = input("Enter the second number: ")

# This converts the second number from string to float
second_number = float(second_number)

# This prompts the user to enter the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on user input
if operation == '+':
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif operation == '-':
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif operation == '*':
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif operation == '/':
    if second_number != 0:  # Check for division by zero
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation. Please enter one of +, -, *, or /.")
