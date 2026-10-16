with open("/content/sample_data/data.txt", "r") as file:
  content = file.read().split()
  content = list(map(lambda x: x.strip("."), content))

  the_longest_word = content[0]

  for word in content:
    if len(word) > len(the_longest_word):
      the_longest_word = word

  print(the_longest_word)