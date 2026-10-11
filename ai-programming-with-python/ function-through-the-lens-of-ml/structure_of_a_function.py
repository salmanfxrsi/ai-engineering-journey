# Parameter with Default Value
def welcome_message(name = "Guest"):
    print(f"Hello, {name}! Welcome to the program.")

welcome_message("Alice") # Output: Hello, Alice! Welcome to the program.
welcome_message() # Output: Hello, Guest! Welcome to the program.


# Function with return value and documentation
def add_numbers(a = 0, b = 0):
    """
    Adds two numbers
    a: int
    b: int
    """
    return a + b

print(add_numbers(5, 10))  # Output: 15
print(add_numbers(5))       # Output: 5
print(add_numbers())        # Output: 0
help(add_numbers) # Output: Help on function add_numbers in module __main__: