# A word is called a Palindrome if reversing its letters results in the same word (ignoring case). Write a program to check whether a given string is a palindrome.

# Input Format:
# A single word string

# Output Format:
# "Palindrome" or "Not Palindrome"

# Example:
# Input:
# Radar

# Output:
# Palindrome

# Implementation
word = input().lower()
word_list = list(word)
reverse_word_list = []

for n in range(len(word) - 1, -1, -1):
  reverse_word_list.append(word[n])

if word_list == reverse_word_list:
  print("Palindrome")
else:
  print("Not Palindrome")