"""
TODO 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se
 digitar outro valor deve aparecer valor inválido.
"""


def calendar():
    name = "WEEK CALENDAR"
    print(f"{name:#^20}")
    d = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
    c = 1
    for item in d:
        print(f"{c}-{item}")
        c += 1
    opt = int(input("Choose an option: "))
    if opt <= 0 or opt > 7:
        print("Wrong choice. Try again.")
        calendar()
    elif opt > 0 <= 7:
        print(f"You choose {d[opt-1]}")


calendar()
