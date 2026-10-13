with open("./test.txt", "w") as file: 
    file.write("Hello, this is test file\n")
    file.write("How is learning going on?\n")

# writing on a existing file (it overwrites the file)

with open("./test.txt", "w") as file: 
    file.write("Hey, this is second attempt\n")
    file.write("Learning is going so fast\n")

# no overwriting just append the text later (append mode)

with open("./test.txt", "a") as file: 
    file.write("The learning of AI/ML is fun\n")
    file.write("I'm enjoying it so much\n")

with open("./test.txt", "r") as file:
    content = file.readlines()
    content = list(map(str.strip, content))
    print(content)
