def dot(cl):
    c = len(color_list)
    while c > 0:
        while cl > 0:
            new_color = alper.color(c)
            alper.pendown()
            alper.dot(new_color)
            alper.penup()
            alper.forward(dist)
            cl -= 1
    c -= 1

for col in range(16):
    dot(col)
    for line in range(10):
        alper.penup()
        y -= dist
        alper.sety(y)
        alper.pendown()