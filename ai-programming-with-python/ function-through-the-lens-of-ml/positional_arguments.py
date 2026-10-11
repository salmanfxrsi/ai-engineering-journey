def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum(30, 42, 42, 22, 98))