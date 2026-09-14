# You’re simulating an ensemble of mini-models that each vote YES or NO on admitting a user. Read how many votes there are, then read each vote. If the number of YES votes is greater than or equal to the number of NO votes, print ACCEPT; otherwise print REJECT.
# New concept — Ensemble majority voting
# Several weak opinions can combine into one stronger decision

n = int(input("Enter the number of votes: "))

votes = []

for i in range(n):
    votes.append(input(f"Enter vote {i+1}: "))

yes_votes = 0
no_votes = 0

for i in range(n):
    if votes[i] ==   "YES":
        yes_votes += 1
    else: 
        no_votes += 1
        
if yes_votes >= no_votes:
    print("ACCEPT")
else: 
    print("REJECT")
