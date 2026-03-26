# Simple calculator for two numbers

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Output results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
