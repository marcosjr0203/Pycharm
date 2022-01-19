from turtle import Turtle, Screen

jack = Turtle()
jack.shape("arrow")
length = 20
# That was my 'solution'
# def dash():
#     jack.forward(10)
#     jack.color("white")
#     jack.forward(10)
#     jack.color("black")

# Now I present the real solution


def dash():
    jack.forward(10)
    jack.penup()
    jack.forward(10)
    jack.pendown()


while length > 0:
    dash()
    length -= 1


screen = Screen()
screen.exitonclick()
