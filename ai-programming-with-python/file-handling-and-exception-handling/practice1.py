# Practice 1 :

# Get the text from sample.txt , and count the following

# Number of lines

# Number of words

# Number of characters

# and save it to the counter_of_string.txt file


# Solution

from functools import reduce

with open("./sample.txt", "r") as file:

    # read file by lines
    strings = file.readlines()
    
    # total lines
    total_number_of_lines = len(strings) 

    # total words 
    number_of_words = list(map(lambda x : len(x.split()), strings))
    total_number_of_words = reduce(lambda x, y: x + y, number_of_words)

    # cleaning process

    ## 1. new line delete
    strings = list(map(lambda x: x.rstrip("\n"), strings))
    

    ## number of character 
    number_of_character = list(map(lambda x: len(x), strings))

    ## total number of character
    total_number_of_character = reduce(lambda x, y: x + y, number_of_character)

    
    with open("./counter_of_string.txt", "w") as file:
        file.write(f"Total number of lines: {total_number_of_lines}\n")
        file.write(f"Total number of words: {total_number_of_words}\n")
        file.write(f"Total number of characters: {total_number_of_character}\n")

