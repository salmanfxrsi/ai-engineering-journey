sum = 0

for i in range(1, 11):

    print(i, "is processing...")

    if i % 2 == 0: # Check if the number is even
        continue # Skip the rest of the loop for even numbers

    sum += i # Add odd numbers to the sum
    
print("The sum of odd numbers from 1 to 10 is: ", sum)


accuracy = 95

for i in range(20):
    accuracy += 1
    print("Current accuracy: ", accuracy)
    if accuracy == 100:
        break # Exit the loop if accuracy reaches 100