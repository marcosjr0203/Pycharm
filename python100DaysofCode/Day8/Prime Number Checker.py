"""
100 DAYS OF CODE
DAY 8
Write a program that checks if a given number is or is not a prime number
Use a function with input to verify that.
"""
# n = int(input("Enter the number: "))
#
#
# def prime_checker(num):
#     if num % 2 == 0 and num != 2 \
#             or num % 3 == 0 and num != 3 \
#             or num % 5 == 0 and num != 5 \
#             or num % 7 == 0 and num != 7:
#         print(f"{num} is not a prime number.")
#     else:
#         print(f"{num} is a prime number.")
#
#
# prime_checker(n)

# Teacher's way:
# e.g.: if the number is 59, the program verifies if 59 % 2,59 % 3...59 % 58==0, if it is, then it's not a prime number.
n = int(input("Enter the number: "))


def prime_checker(num):
    prime = True
    for i in range(2, num-1):
        if num % i == 0:
            prime = False
    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


prime_checker(n)
