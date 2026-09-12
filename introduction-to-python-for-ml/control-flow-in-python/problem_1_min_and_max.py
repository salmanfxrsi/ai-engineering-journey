inp = input("Enter a list of numbers separated by spaces: ")
numbers = inp.split()

x = int(numbers[0])
y = int(numbers[1])
z = int(numbers[2])

# min
min = x

if y < min: 
    min = y

if z < min: 
    min = z

# max
max = x

if y > max: 
    max = y

if z > max: 
    max = z


print("The minimum number is:", min)
print("The maximum number is:", max)