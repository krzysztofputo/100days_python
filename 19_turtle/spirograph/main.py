from turtle import *
from random import randint


def rand_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


colormode(255)
t = Turtle()
t.penup()
t.speed('fastest')
t.goto(-50, 100)
t.pendown()

x = 5
while x != 360:
    t.color(rand_colors())
    t.circle(100)
    x += 5
    t.setheading(x)

exitonclick()
