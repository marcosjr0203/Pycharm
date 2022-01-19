"""
100 DAYS OF CODE
DAY 10
 TODO-1 Write a function that asks for a year and a month as input.
  The output has to be the number of the days in a month, considering one more day, if the year is a leap year.
"""
numdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nummont = ["January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December"]


def leap_year(y):
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
