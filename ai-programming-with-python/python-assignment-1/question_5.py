word = input().lower()
word_list = list(word)
reverse_word_list = []

for n in range(len(word) - 1, -1, -1):
  reverse_word_list.append(word[n])

if word_list == reverse_word_list:
  print("Palindrome")
else:
  print("Not Palindrome")