fruits = ["apple", "banana", "cherry"]

capitalized_fruits = []

for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize())

print(capitalized_fruits)

upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)