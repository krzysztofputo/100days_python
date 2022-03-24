import turtle as tu

from random import *
t = tu.Turtle()
tu.colormode(255)
t.penup()
t.goto(-50,200)
t.pendown()
x = 3
for _ in range(10):
    for __ in range(x):
        angles = 360 / x
        t.forward(100)
        t.right(angles)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    x += 1
    t.color(color)

