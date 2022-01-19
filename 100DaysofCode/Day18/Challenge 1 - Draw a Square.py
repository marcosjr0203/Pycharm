import random
from turtle import Turtle, Screen
import random
# accesse: docs.python.org/3/library/turtle.html mais informações sobre o 'Turtle'
marvin = Turtle()
marvin.color("black")
print(marvin.shape("turtle"))
d = 0
for _ in range(4):
    marvin.forward(100)
    marvin.left(90)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()