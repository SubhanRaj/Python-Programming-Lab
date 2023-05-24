# Program to Implement Simple Calculator in Python

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# Display calculator menu
print("Calculator Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user's choice
choice = input("Enter your choice (1-4): ")

# Perform selected operation based on user's choice
if choice in ['1', '2', '3', '4']:
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        # Addition
        result = add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        # Subtraction
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        # Multiplication
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        if num2 != 0:
            # Division
            result = divide(num1, num2)
            print("Result:", result)
        else:
            # Division by zero error handling
            print("Cannot divide by zero!")
else:
    # Invalid choice error handling
    print("Invalid choice!")
