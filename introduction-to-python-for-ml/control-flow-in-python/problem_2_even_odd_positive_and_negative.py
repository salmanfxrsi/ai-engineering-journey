n = int(input("Enter size: "))

numbers = input("Enter numbers separated by space: ").split()

even = 0
odd = 0
positive = 0
negative = 0

for i in range(n): 
    number = int(numbers[i])

    if number % 2 == 0:
        even += 1
    else: 
        odd += 1
    
    if number > 0:
        positive += 1
    elif number < 0: 
        negative += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Positive numbers:", positive)
print("Negative numbers:", negative)