from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.x_move = 10
        self.y_move = 10
        self.line()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
        self.bounce_y()

    def line(self):
        self.goto(0, 290)
        self.setheading(270)
        for i in range(29):
            if i % 2 == 0:
                self.pendown()
                self.forward(20)
            else:
                self.penup()
                self.forward(20)
        self.penup()
