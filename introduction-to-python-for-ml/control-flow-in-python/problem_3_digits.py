t = int(input("Enter the number of tests: "))

for i in range(t):
    number = int(input("Enter number: "))
    
    while number > 0:
        print(number % 10, end = " ")
        number //= 10
    print()
