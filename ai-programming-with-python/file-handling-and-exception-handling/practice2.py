# Practice 2

# Write then read with one open


# Solution
with open("./write_read.txt", "w+") as file:
    file.write("Hello world!")

    print(file.tell())

    file.seek(0)
    print(file.tell())

    print(file.read())

    file.truncate(5)

    file.seek(0)

    print(file.read())