import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

t = turtle.Turtle()
t.color("black")
t.hideturtle()
t.penup()
score = Scoreboard()
player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.cars_move()
    for i in car.cars_list:
        if player.distance(i) < 20:
            t.write(f"You reached level {score.level}", align="center", font=("Courier", 30, "bold"))
            game_is_on = False
    if player.ycor() > 280:
        player.next_level()
        score.next_level()
        car.increase_speed()

screen.exitonclick()