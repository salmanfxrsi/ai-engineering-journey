# Given a list of integers, extract all numbers that are divisible by 4 but not divisible by 8.

# Input Format:
# Space-separated integers

# Output Format:
# A list of numbers satisfying the condition

# Example:
# Input:
# 4 6 8 12 16 20 24 28 

# Output:
# [4, 12, 20, 28] 

# Implementation
numbers = input("write a list of integers here: ").split()
output = []

for number in numbers:
  if int(number) % 4 == 0 and int(number) % 8 !=0:
    output.append(int(number))

print(output)
