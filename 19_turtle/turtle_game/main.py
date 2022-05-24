from turtle import Turtle, Screen
from random import randint

t = Turtle()
screen = Screen()
screen.setup(500, 400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

cord_list = [(-240, -100), (-240, -50), (-240, 0), (-240, 50), (-240, 100)]
color_list = ["red", "blue", "green", "yellow", "black"]
all_turtles = []
for i in range(5):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color_list[i])
    turtle.goto(cord_list[i])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"Congratulation you have won! {winning_color} is the winner!")
            else:
                print(f"You have lost! {winning_color} is the winner!")

        rand_forward = randint(0, 10)
        t.forward(rand_forward)


screen.exitonclick()
