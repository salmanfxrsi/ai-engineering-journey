# In real AI systems, mood detection uses natural language processing (NLP) to understand emotions from text. For now, let's simulate a mini version of that!
# You are given a sentence that represents a user's message. Your job is to guess if the mood is happy, sad, or neutral using simple logic:
# If the message contains words like happy, joy, or smile, print Happy Mood.
# If it contains words like sad, cry, or angry, print Sad Mood.
# Otherwise, print Neutral Mood.

message = input("Put your message here: ").lower().split()

output = ""

for i in message:
    if i in ['happy', 'joy', 'smile']:
        output = "Happy Mood"
    elif i in ['sad', 'cry', 'angry']:
        output = "Sad Mood"

print(output if output else "Neutral Mood")
