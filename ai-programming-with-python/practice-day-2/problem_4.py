# Problem 4  Read from a Specific File Pointer Position

# Write a function read_from_position(filename, position) that uses the file pointer to start reading a file from a given byte position and prints the remaining content.

# Sample Input:
# filename = "hello.txt"   # contains: "Hello, World!"
# position = 7

# Sample Output:
# World!

def read_from_position(filename, position):
    with open(f"./sample_data/{filename}", "r") as file:
        file.seek(position)
        print(file.read())

read_from_position("hello.txt", 7)