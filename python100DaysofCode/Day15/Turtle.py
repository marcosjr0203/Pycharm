from turtle import Turtle, Screen
from random import randint
# accesse: docs.python.org/3/library/turtle.html mais informações sobre o 'Turtle'

num = 20
c = 0
fibonacci = [0, 1]
while c <= num:
    next_term = int(fibonacci[c])+int(fibonacci[c+1])
    fibonacci.append(next_term)
    c += 1
marvin = Turtle()
neto = Turtle()
michel = Turtle()
marvin.color("black")
neto.color("blue")
michel.color("red")
print(marvin.shape("turtle"))
print(neto.shape("turtle"))
print(michel.shape("turtle"))
d = 0
for item in fibonacci:
    while d <= len(fibonacci):
        var = randint(1, 101)
        marvin.forward(var)
        neto.left(90)
        neto.forward(var)
        michel.left(90)
        michel.forward(var)
        neto.left(90)
        neto.forward(var)
        marvin.forward(var)
        marvin.left(90)
        michel.forward(var)
        michel.left(90)
        marvin.forward(var)
        marvin.left(90)
        neto.forward(var)
        marvin.forward(var)
        neto.left(90)
        michel.forward(var)
        michel.left(90)
        marvin.forward(var)
        neto.left(90)
        neto.forward(var)
        marvin.forward(var)
        marvin.left(90)
        michel.forward(var)
        neto.left(90)
        marvin.forward(var)
        michel.left(90)
        neto.forward(var)
        d += 1

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()