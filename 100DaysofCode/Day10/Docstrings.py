"""
100 DAYS OF CODE
DAY 10
"""
numdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nummont = ["January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December"]


def leap_year(y):
    """ Take a year (YYYY) and returns 'True' if it is leap, otherwise returns 'False'"""
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(d, m):
    """ Take a month from a given year and returns how many days it has"""
    if m == 2:
        if leap_year(y=year):
            d += 1
            return d
        else:
            return d


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
days = days_in_month(d=numdays[month-1], m=month)
print(f"{nummont[month-1]} of {year} has {days} days.")
