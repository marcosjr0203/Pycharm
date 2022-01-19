"""
Write a program that calculates the high score from a list of scores.
"""
n = input("Enter the scores, separated by a comma: ").split(",")
scores = []
for item in n:
    item = int(item)
    scores.append(item)
highest = 0
for i in scores:
    if scores[i] > highest:
        highest = scores[i]
print(f" The highest score is {highest}")
