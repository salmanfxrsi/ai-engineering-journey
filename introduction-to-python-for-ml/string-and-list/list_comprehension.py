even = []

## naive
for i in range(100):
    if i % 2 == 0:
        even.append(i)

print(even)

## list comprehension
odd = [x for x in range(100) if x % 2 != 0]
print(odd)
