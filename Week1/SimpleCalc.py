# Functions for each operation 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Undefined number (division by zero)."
    return a / b


# Main Program 

print("Project Simple Calculator")
print("Operators:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get input from user
choice = input("Enter an operator of your choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# Use if-elif to choose the operation
if choice == "1":
    result = add(num1, num2)
elif choice == "2":
    result = subtract(num1, num2)
elif choice == "3":
    result = multiply(num1, num2)
elif choice == "4":
    result = divide(num1, num2)
else:
    result = "Invalid choice!"

print("The result of the calculation is:", result)
