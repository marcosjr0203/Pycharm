"""
Develop a program that:
 1- asks for the total bill;
 2- asks for the percentage of tip you wish to give (10, 12 or 15);
 3- asks for how many people will split the bill;
 4- give the amount that each person should pay.
"""
tb = float(input("Enter the total bill: "))
p = int(input("Which percentage of tip you wish to give: 10, 12 or 15? "))
n = int(input("How many will split the bill? "))
print(f"Each one should pay ${tb + (tb*p/100/n):.2f}")
