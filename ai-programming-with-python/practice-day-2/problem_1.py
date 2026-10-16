# Problem 1  Create and Write to a File

# Write a function create_file(filename, content) that creates a new text file with the given filename and writes the content into it. Call it using positional arguments.

# Sample Input:
# "notes.txt", "Hello, this is my first file."

# Sample Output (notes.txt will contain):
# Hello, this is my first file.

# Implementation
def create_file(filename, content):
    with open(f"./sample_data/{filename}", "w") as file: 
        file.write(content)

create_file("notes.txt", "Hello, this is my first file.")

