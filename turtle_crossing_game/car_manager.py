from turtle import Turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.cars()
        self.speed = STARTING_MOVE_DISTANCE

    def cars(self):
        for i in range(20):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(randint(-200, 260), randint(-250, 260))
            self.cars_list.append(car)

    def cars_move(self):
        for i in self.cars_list:
            new_x = 0
            new_x = i.xcor() - self.speed
            i.goto(new_x, i.ycor())

            if i.xcor() < -320:
                i.goto(280, randint(-250, 260))

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
