# Write a program that converts a sentence into a list of words but only includes words that start with a vowel (a, e, i, o, u), ignoring case.

# Input Format:

# A single line sentence

# OutputFormat:
# A list of strings

# Example:

# Input:
# An apple a day keeps the doctor away

# Output:
# ['An', 'apple', 'a', 'away']

# Implementation
sentence = input("write sentence here: ").split()
output = []

for word in sentence:
  list_word = list(word)
  if list_word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    output.append(word)

print(output)