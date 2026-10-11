# return integer
def add(a, b):
    return a + b

print(type(add(2, 3)))  # Output: <class 'int'>


# return float
def divide(a, b):
    return a / b

print(type(divide(5, 2)))  # Output: <class 'float'>


# return string
def concatenate(a, b):
    return str(a) + str(b)

print(type(concatenate(2, 3)))  # Output: <class 'str'>


# return list
def create_list(*args):
    return list(args)

print(type(create_list(1, 2, 3)))  # Output: <class 'list'>


# return tuples
def create_tuple(*args):
    return tuple(args)

print(type(create_tuple(1, 2, 3)))  # Output: <class 'tuple'>
