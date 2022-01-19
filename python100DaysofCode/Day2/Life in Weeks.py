"""
Create a program that ask user's age and calculate how many days, week and months he has until 90 years old.
"""
age = int(input("Insert your current age: "))
y = 90 - age
m = y*12
w = m*4
d = w*7
h = d*24
min = h*60
s = min*60
print(f"You have: \n"
      f"{y} years, \n"
      f"{m} months, \n"
      f"{w} weeks, \n"
      f"{d} days, \n"
      f"{h} hours, \n"
      f"{min} minutes and \n"
      f"{s} seconds\n"
      f"left until you're 90.")