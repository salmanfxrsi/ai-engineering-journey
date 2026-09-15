# Dictionary: A collection of key-value pairs

## Empty Dictionary
D = {}
print(type(D))

D = {"name": "Salman Farsi", "age": 19, "address": "Sylhet, Bangladesh", "numbers": [10, 20, 30]}
print(type(D), D)

## Access 
print(D["numbers"])
print(D.get("age"))

D["age"] = 20
D = {"name": "Salman Farsi", "age": 19, "address": "Sylhet, Bangladesh", "numbers": [10, 20, 30], "age": 30}
print(D)

