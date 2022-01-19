import turtle
from turtle import Turtle, Screen
import random
turtle.penup()
turtle.sety(-300)
turtle.pendown()
turtle.speed(0)

def shape(ang, sid, col):
    while sid > 0:
        turtle.forward(1)
        turtle.left(ang)
        turtle.color(col)
        turtle.fillcolor(col)
        sid -= 1


shapes = int(input("How many shapes do you wanna see? "))
sides = 3
colors = ["green", "purple", "gold", "orange", "red",
          "maroon", "violet", "magenta", "purple",
          "navy", "blue", "skyblue", "cyan", "turquoise",
          "lightgreen", "green", "darkgreen", "chocolate",
          "brown", "black", "gray"]
while shapes > 0:
    angle = 360/sides
    shape(angle, sides, colors[random.randint(0, len(colors)-1)])
    sides += 1
    shapes -= 1
screen = Screen()
screen.exitonclick()
