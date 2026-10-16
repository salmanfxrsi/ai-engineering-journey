# Write a Python program that reads a text file and finds the longest word.

# Requirements:

# Open and read data from a file (Example: data.txt)
# If multiple words have the same longest length, print any one of them


# Input Format:
# A text file containing multiple lines of text

# Output Format:
# The longest word

# Example File Content (data.txt):
# Python is a wonderful language for machine learning.

# Output:
# wonderful

# Implementation
with open("/content/sample_data/data.txt", "r") as file:
  content = file.read().split()
  content = list(map(lambda x: x.strip("."), content))

  the_longest_word = content[0]

  for word in content:
    if len(word) > len(the_longest_word):
      the_longest_word = word

  print(the_longest_word)