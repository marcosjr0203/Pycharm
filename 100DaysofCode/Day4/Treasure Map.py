"""
Write a program which will mark a spot in a matrix with an "x"
Your program shoul allow the user to enter the position of the treasure through lines and columns system.
"""
row1 = ["◙", "◙", "◙"]
row2 = ["◙", "◙", "◙"]
row3 = ["◙", "◙", "◙"]
map = [row1, row2, row3]


def ask():
    print(f"{row1}\n{row2}\n{row3}")
    line, col = input("Type the line (1-3) and column (1-3) where do you want to "
                      "hide your treasure, separated by a comma: ").split(",")
    line, col = int(line), int(col)
    if line == 1:
        row1[col-1] = "X"
    elif line == 2:
        row2[col-1] = "X"
    elif line == 3:
        row3[col-1] = "X"
    elif line > 3 or line <= 0 or col > 3 or col <= 0:
        print("Wrong answer.\nStart again.")
        ask()
    print(f"{map[0]}\n{map[1]},\n{map[2]}")


ask()
