sentence = input("write sentence here: ").split()
output = []

for word in sentence:
  list_word = list(word)
  if list_word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    output.append(word)

print(output)