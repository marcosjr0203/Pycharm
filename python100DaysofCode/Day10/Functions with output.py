"""
100 DAYS OF CODE
DAY 10
"""
# def my_function():
#     result = 3*2
#     return result  # the return replace the function calling
#
#
# my_function()  # will be replaced by '6', as the function returned.
#
#
# """
# TODO Write a function that change the first and second name rewriting them with capital letters.
#  Make the function return the variables.
# """
# # First Mode: the inputs are the variables, with the function being called above the input and replaced by 'return'
#
#
# def format_name(fn, sn):
#     fn, sn = fn.title(), sn.title()
#     return fn, sn
#
#
# fname, sname = input("Enter your first and second name: ").split(" ")
# print(format_name(fname, sname))
#
# # Second Mode: The function is called by a variable which is printed at last
#
#
# def format_name(fn, sn):
#     fn, sn = fn.title(), sn.title()
#     return fn, sn
#
#
# fname, sname = input("Enter your first and second name: ").split(" ")
# formatted_name = format_name(fname, sname)
# print(formatted_name)
#
#
# # Third Mode: the function returns is the print of the formatted names (Will be printed without quotes)
#
#
# def format_name(fn, sn):
#     fn, sn = fn.title(), sn.title()
#     return print(fn, sn)
#
#
# fname, sname = input("Enter your first and second name: ").split(" ")
# format_name(fname, sname)
#
# # Fourth Mode: function called with the inputs
#
#
# def format_name(fn, sn):
#     fn, sn = fn.title(), sn.title()
#     return print(fn, sn)
#
#
# format_name(fn=input("Enter your first name: "), sn=input("Enter your second name: "))

# Fifth Mode: with multiple return values


def format_name(fn, sn):
    if fn == "" or sn == "":
        if not fn == "":
            fn = fn.title()
            return print(fn)
        elif not sn == "":
            sn = sn.title()
            return print(sn)
    else:
        fn, sn = fn.title(), sn.title()
        return print(fn, sn)


format_name(fn=input("Enter your first name: "), sn=input("Enter your second name: "))

