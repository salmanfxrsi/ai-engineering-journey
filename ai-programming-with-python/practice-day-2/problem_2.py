# Problem 2  Read Lines with Line Numbers

# Write a function read_lines(filename) that reads a text file and prints each line with its line number.

# Sample Input (file: data.txt):
# Apple
# Banana
# Cherry

# Sample Output:
# 1: Apple
# 2: Banana
# 3: Cherry

# Implementation
def read_lines(filename):
    with open(f"./sample_data/{filename}", "r") as file:
        content = file.readlines()
        counter = 1
        for sentence in content:
            print(f"{counter}: {sentence}")
            counter += 1

read_lines("data.txt")

