from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"{self.p1_score}        {self.p2_score}", move=False, align=ALIGNMENT, font=('Courier', 40, 'normal'))

    def p1_scores(self):
        self.p1_score += 1
        self.update_score()

    def p2_scores(self):
        self.clear()
        self.p2_score += 1
        self.update_score()
