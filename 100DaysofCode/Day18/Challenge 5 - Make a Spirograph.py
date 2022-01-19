import turtle
from turtle import Turtle, Screen
import random
marvin = Turtle()
marvin.speed(0)
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for _ in range(1000):
    marvin.heading()
    marvin.left(0.35150625)
    marvin.circle(100)
    marvin.color(random_color())

screen = Screen()
screen.exitonclick()
