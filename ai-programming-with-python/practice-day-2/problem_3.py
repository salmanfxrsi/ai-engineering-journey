# Problem 3  Append Log Entries to a File

# Given a filename log.txt, use file append mode to add a new log entry each time the function add_log(message) is called. Each message should appear on a new line.

# Sample Input:
# add_log("User logged in")
# add_log("File uploaded")

# Sample Output (log.txt will contain):
# User logged in
# File uploaded

def add_log(message):
    with open("./sample_data/log.txt", "a") as file:
        file.write(message + "\n")

add_log("User logged in")
add_log("File uploaded")





