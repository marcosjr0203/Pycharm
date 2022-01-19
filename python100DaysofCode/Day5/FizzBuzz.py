"""
Write a program that prints each number from 1 to 100 in turn.
When the number is divisible by 3, then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".
and if the number is fivisible by both, 3 and 5, e.g. 15, then instead of the number it shoud print "FizzBuzz".
"""
for item in range(0, 101):
    if item % 3 == 0:
        if item % 5 != 0:
            print(f"{item} - Fizz")
        else:
            print(f"{item} - FizzBuzz")
    elif item % 5 == 0:
        print(f"{item} - Buzz")
    else:
        print(item)