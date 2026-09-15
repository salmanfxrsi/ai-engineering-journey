D = {"name": "Salman Farsi", "age": 19, "address": "Sylhet, Bangladesh", "numbers": [10, 20, 30]}


print(D["numbers"])
print(D.get("age"))

D["age"] = 20
print(D)

print(D.get("math_marks"))
print(D.get("math_marks", 0))

# Adding a new key value pair
D["math_marks"] = 95

D.update({"science_marks": 90, "english_marks": 85})

print(D)

# Deleting a key value pair
del D["math_marks"]
print(D)

# Copying the dictionary
D_copy = D.copy()
print(D_copy)

# Clearing the dictionary
D.clear()
print(D)

# Testing (Note: Keys must be immutable)
D3 = {(1, 2) : "b"}
print(D3)
