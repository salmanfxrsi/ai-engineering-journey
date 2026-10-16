# Write a function compute_ratio(x, y) that returns (x + y) / (x * y). Use exception handling to manage division by zero.
# Use exception handling to manage:
# Division by zero

# Input Format:
# Two values

# Output Format:
# Computed result OR error message

# Implementation
x = int(input("value of x: "))
y = int(input("value of y: "))

def compute_ratio(x, y):
  try:
    return (x + y) / (x * y)
  except ZeroDivisionError:
    return "Error: Division not possible"

print(compute_ratio(x, y))