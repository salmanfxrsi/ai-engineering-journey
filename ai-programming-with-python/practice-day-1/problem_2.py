# Write a Python generator function called batch_generator. It should take a list of numbers (representing data samples) and a batch_size. The generator should yield one batch at a time as a list.

# Example Input:
# data = [1, 2, 3, 4, 5, 6, 7, 8]
# batch_size = 3

# Expected Output (when iterated):
# [1, 2, 3]
# [4, 5, 6]
# [7, 8]

# Implementation
def batch_generator(numbers, batch_size):
    yield 

batch_generator([1, 2, 3, 4, 5, 6, 7, 8], 3)
