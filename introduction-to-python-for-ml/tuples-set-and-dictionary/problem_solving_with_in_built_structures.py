# 1. Given a list of numbers, make a list with unique values
numbers = [10 ,20 , 10, 30, 30, 50, 30, 10, 20, 10, 10]
unique_numbers = set(numbers)
list_numbers = list(unique_numbers)

print(list_numbers)

# 2. Given a string , print the frequency of the words
string = """data science machine learning data analysis machine 
learning statistics data models data training data validation features
features labels preprocessing data augmentation models data optimization 
gradient descent neural networks data tensors matrices visualization 
exploration pandas numpy matplotlib seaborn scikit-learn tensorflow pytorch 
deployment inference production monitoring reproducibility experiments results 
metrics accuracy precision recall f1 cross validation data machine
"""

words = string.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

for k,v in count.items():
    print(f"{k} : {v}")