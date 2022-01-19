import turtle
import another_module
import prettytable
#docs.python.org/3/library/turtle.html/#turtle.color
print(another_module.another_variable)
timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
# timmy = turtle.Turtle()
# object = module.Class()
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
star_trek = prettytable.PrettyTable()
star_trek.add_column("Name", ["Kirk", "Spock", "Uhura"])
star_trek.add_column("Function", ["Capitain", "Immediate", "Comunicator"])
star_trek.align = "l"
print(star_trek)

