file = open("example.txt", "r")
content = file.readlines()
print(type(content))
print(content)

file.close()

with open("./example.txt", "r") as file:
    content = file.readlines()
    print(content)

print(file.closed)

with open("./example.txt", "r") as file: 
    for line in file:
        f = line.strip()