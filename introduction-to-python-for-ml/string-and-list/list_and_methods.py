# List is a collection of data
# Lists are ordered, mutable and allow duplicate elements

numbers = [100, 20, 43, 42, 94]

## accessing elements in a list
print(numbers[0]) 

numbers[2] = 99
print(numbers) 

new_list = numbers[0:3]
print(new_list)

## adding elements to a list
numbers.append(55)
print(numbers)

## insertion at any index
numbers.insert(2, 88)
print(numbers)

## removing elements from a list
numbers.remove(42)
print(numbers)

numbers.pop()
print(numbers)

## declaration
mixed_list = [100, "Hello", 3.14, True]
print(mixed_list)

## 2D List
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(two_d_list)
