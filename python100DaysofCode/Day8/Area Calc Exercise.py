"""
100 DAYS OF CODE
DAY 8
Create a program that calculates how many cans of paint you'll need, given height and weight of a wall, considering
that a can paints 5 squared meters of wall.
"""


def paint_calculator(h, w, c):
    coverage = h*w/c
    print(f"You'll need {round(coverage)} can", end="")
    print("s of paint.") if coverage > 1 else print(" of paint.")


height = float(input("Insert the height (m²): "))
weight = float(input("Insert the weight (m²): "))
coverture = int(input("Insert the coverture (m²): "))
paint_calculator(h=height, w=weight, c=coverture)
