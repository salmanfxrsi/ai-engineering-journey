# declaration
tup = (10, 20, 30, 40, 50, 60)
float_tup = (10.5, 10.2)
mixed_tup = (10, 10.5, "programming", True)

list = [10, 20, 30]
list_to_tuple = tuple(list)

print(type(list_to_tuple), list_to_tuple)

# access elements
print(tup[0], float_tup[1], mixed_tup[2])

# slicing
print(tup[1:4], float_tup[:1], mixed_tup[2:])

# mutable 
lst = [10, 20, 30, 40]
lst.append(50)
lst[1] = 100
print(lst)

# immutable
tup = (10, 20, 30, 40)
# tup[1] = 100
print(tup)

# tuple method
print(tup.count(20), tup.index(30))