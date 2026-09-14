# AI systems often scan user messages to find keywords and understand intent. Let’s build a simple version of that!
# You are given a user's message and a list of AI-related keywords. Your task is to count how many of those keywords appear in the message.
# The keywords to look for are:
# ai, data, model, learn, train, neural
# If 2 or more keywords are found, print AI Detected. Otherwise, print Not AI Related.

message = input("test your message: ").lower().split()

number_of_keyword = 0

for word in message: 
    if word in ["ai", "model", "data", "learn", "train", "neural"]:
        number_of_keyword += 1

if number_of_keyword >= 2:
    print("AI Detected")
else:
    print("Not AI Related") 