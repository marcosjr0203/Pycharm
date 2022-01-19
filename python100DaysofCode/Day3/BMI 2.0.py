"""
Create a BMI calculator.
"""
weight, height = input("Enter your weight and height, separated by a comma: ").split(",")
weight = float(weight)
height = float(height)
BMI = weight/height**2
if BMI < 18:
    print(f"Your BMI is {BMI:.2f}. You're underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI:.2f}. You are at your ideal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI:.2f}. You are overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI:.2f}. You are obese.")
else:
    print(f"Your BMI is {BMI:.2f}. You're clinically obese.")