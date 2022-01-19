"""
Create a program to calculate the average height from a list.
"""
avlist = [1.75, 1.69, 1.95, 1.59, 1.77, 1.82, 1.67, 1.70, 1.77, 1.79, 1.84]
sum = 0
for item in avlist:
    sum += item
print(f"Average: {sum/len(avlist):.2f}")
