from turtle import Turtle, Screen
import random
jack = Turtle()
jack.pensize(10)
jack.speed(0)
colors = ["green", "purple", "gold", "orange", "red",
          "maroon", "violet", "magenta", "purple",
          "navy", "blue", "skyblue", "cyan", "turquoise",
          "lightgreen", "green", "darkgreen", "chocolate",
          "brown", "black", "gray"]
# duration = 10000
# def way():
#     direction = 0, 90, 180, 270
#     head = random.choice(direction)
#     jack.setheading(head)
#     jack.forward(30)
#     jack.color(random.choice(colors))
#
#
# while duration > 0:
#     way()
#     duration -= 1
# screen = Screen()
# screen.exitonclick()

# Dr. Angela's way:
direction = 0, 90, 180, 270
for _ in range(200):
    jack.color(random.choice(colors))
    jack.forward(30)
    jack.setheading(random.choice(direction))
