n = int(input("Enter number of losses: "))
target = float(input("Enter target loss: "))

losses = []

for i in range(n):
    losses.append(float(input(f"Enter loss {i+1}: ")))
    
sum = 0

for loss in losses: 
    sum += loss

average = sum / n

if average <= target:
    print("PASS")
else: 
    print("RETRY")