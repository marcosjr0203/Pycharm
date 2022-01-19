import turtle
from turtle import Turtle, Screen
import random
marvin = Turtle()
marvin.speed(15)
turtle.colormode(255)

#TODO.1 Randomize RGB colors
def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

direction = (0, 90, 180, 270)

#TODO.2 Create a Random Walk
for _ in range(1000):
    marvin.color(random_rgb())
    marvin.forward(random.randint(0, 10))
    marvin.pensize(random.randint(0, 15))
    marvin.setheading(random.choice(direction))



screen = Screen()
screen.exitonclick()