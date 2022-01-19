"""
100 DAYS OF CODE
DAY 10
TODO-1 Create a calculator using functions for each mathematical operations
TODO-2 Create a dictionary with the operators
"""


def add(n1, n2):
    """Add"""
    return n1+n2


def sub(n1, n2):
    """Subtract"""
    return n1-n2


def mult(n1, n2):
    """Multiply"""
    return n1*n2


def div(n1, n2):
    """Divide"""
    return n1/n2


def is_num(n):
    while not n.isnumeric():
        n = input("Wrong option. Enter a valid number: ")
    return float(n)


def calculator():
    proceed = True
    memory = 0
    num1 = is_num(input("1st number: "))
    num2 = is_num(input("2nd number: "))
    while proceed is True:
        operators = {"+": add, "-": sub, "*": mult, "/": div}
        for item in operators:
            print(item)
        operator = input("Choose operator: ")
        while operator not in "+-/*":
            operator = input("Wrong option. Choose operator: ")
        if operator in operators:
            calc = operators[operator](num1, num2)
            memory += calc
            print(calc)
        cont = input("Continue [y/n]: ")
        while not cont.lower() in "yn":
            print("Wrong Answer. Try again")
            cont = input("Continue [y/n]: ")
        if cont.lower() == "y":
            num1 = calc
            num2 = is_num(input("Next number: "))
        elif cont.lower() == "n":
            print("Thank you for using my fucking calculator.")
            proceed = False

calculator()
