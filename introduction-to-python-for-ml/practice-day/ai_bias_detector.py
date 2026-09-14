# In AI, bias means the model might favor one category more than others. Let’s simulate this idea with lists and conditional logic!
# You are given a list of predictions made by an AI model. Each prediction is either 'A' or 'B'.
# Your task is to check whether the model is biased or fair:
# If the count of 'A' or 'B' is more than 70% of all predictions, print Biased Model.
# Otherwise, print Fair Model.

predictions = input().split()

total_A = 0
total_B = 0
total_prediction = 0

for prediction in predictions:
    total_prediction += 1
    if prediction in ["A"]:
        total_A += 1
    elif prediction in ["B"]:
        total_B += 1

prediction_percentage_A = (total_A / total_prediction)
prediction_percentage_B = (total_B / total_prediction)

if prediction_percentage_A > 0.7 or prediction_percentage_B > 0.7:
    print("Biased Model")
else:
    print("Fair Model")