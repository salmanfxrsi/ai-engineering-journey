#  Write a function power(base, exponent) that returns the result of base raised to exponent. If the exponent is not given, it should calculate the square.

# Sample Input:
# 5

# Sample Output:
# 25

# Sample Input 2:
# 5 3

# Sample Output 2:
# 125

# implementation
def power(base, exponent = 2):
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(power(5))