# calc_with_sympy.py
# Simple calculator using SymPy (open-source math library)

import sympy as sp

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Convert to SymPy numbers
a = sp.Float(num1)
b = sp.Float(num2)

# Perform calculations using SymPy functions
addition = sp.Add(a, b)
subtraction = sp.Sub(a, b)
multiplication = sp.Mul(a, b)
division = sp.Div(a, b) if b != 0 else "Undefined (division by zero)"

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
