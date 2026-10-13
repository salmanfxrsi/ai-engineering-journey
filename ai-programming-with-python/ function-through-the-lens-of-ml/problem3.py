#  Given a list [1,2,3,4], use map() and lambda to create a new list with squares of each number.

# Sample Input:
#  No input

# Sample Output:
# [1, 4, 9, 16]

input = [1, 2, 3, 4]

squared_numbers = map(lambda n: n * n, input)
output = list(squared_numbers)
print(output)







