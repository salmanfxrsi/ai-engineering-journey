# Given a list [1,2,3,4,5,6], use filter() to select even numbers and map() with lambda to square them.

# Sample Input:
#  No input

# Sample Output:
# [4, 16, 36]

# Implementation
numbers = [1,2,3,4,5,6]

numbers = list(filter(lambda x: x % 2 == 0, numbers))
numbers = list(map(lambda x: x * x, numbers))
print(numbers)