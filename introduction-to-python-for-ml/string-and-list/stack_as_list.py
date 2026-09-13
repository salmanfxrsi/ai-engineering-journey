# Stack (LIFO) is implemented as a list in Python. The last element of the list is the top of the stack.

stack = []

## Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

## Pop elements from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

## Check if the stack is empty
print(len(stack) == 0)  # Output: True