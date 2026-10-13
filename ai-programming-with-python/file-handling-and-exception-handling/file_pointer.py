with open("./test.txt", "r") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())
    print(file.read())

with open("./test.txt", "r") as file:
    print(file.tell())
    file.seek(5)
    print(file.tell())
    file.seek(0)

   