# Problem 5 File Read with Full Exception Handling

# Write a function safe_read(filename) that tries to open and read a file. Use try, except, else, and finally blocks:
# Print file content if successful (else block)
# Handle the case where file does not exist (except block)
# Always print "Operation complete." at the end (finally block)

# Sample Input 1:
# safe_read("missing.txt")

# Sample Output 1:
# Error: File not found.
# Operation complete.

# Sample Input 2:
# safe_read("hello.txt")   # contains: "Hello, World!"

# Sample Output 2:
# Hello, World!
# Operation complete.

# Implementation
def safe_read(filename):
    try:
        with open(f"./sample_data/{filename}", "r") as file:
            content = file.read()
    except FileNotFoundError: 
        print("Error: File not found.")
    else:
        print(content)
    finally:
        print("Operation complete.")

safe_read("missing.txt")
safe_read("hello.txt")