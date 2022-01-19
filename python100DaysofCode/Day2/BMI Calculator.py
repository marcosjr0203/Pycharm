"""
Create a BMI calculator.
"""
weight, height = input("Enter your weight and height, separated by a comma: ").split(",")
weight = float(weight)
height = float(height)
BMI = weight/height**2
print(f"Your BMI is {BMI:.2f}.")
