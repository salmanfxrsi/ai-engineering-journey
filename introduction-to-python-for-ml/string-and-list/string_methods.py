string = "welcome to python programming, python is a great language for beginners. python is also used in data science."

print(len(string))  # prints the length of the string
processed_string = string.lower() 
print("python" in processed_string)  # checks if "python" is in the string

start_index = processed_string.find("python") # finds the index of the first occurrence of "python"
print(start_index)

finish_index = processed_string.rfind("python") # finds the index of the last occurrence of "python"
print(finish_index)

count = processed_string.count("python") # counts the occurrences of "python"
print(count)

new_string = string.replace("python", "Java")
print(new_string)
