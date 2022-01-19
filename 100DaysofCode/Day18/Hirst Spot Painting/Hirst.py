from turtle import Turtle, Screen
import turtle
import colorgram
import random
colors = colorgram.extract("image.jpg", 1600)
color_list = []
alper = Turtle()
x = -350
y = 350
dist = 30
alper.penup()
alper.setposition(x, y)
alper.pendown()
alper.pensize(10)
turtle.colormode(255)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    color_list.append(rgb)


def draw_a_line():
    for line in range(16):
        color = alper.color(random.choice(color_list))
        alper.dot(color)
        alper.penup()
        alper.forward(dist)
        alper.pendown()


for lines in range(10):
    draw_a_line()
    alper.penup()
    y -= dist
    alper.setposition(x, y)

screen = Screen()
screen.exitonclick()
