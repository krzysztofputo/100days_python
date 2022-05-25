from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
max_score = screen.numinput("Do ilu gramy?", "", 5, minval=1, maxval=100)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
score = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


t = 0.1
game_is_on = True
while game_is_on:
    time.sleep(t)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        t *= 0.8
    if ball.xcor() > 380:
        score.p1_scores()
        time.sleep(2)
        t = 0.1
        ball.reset_pos()

    if ball.xcor() < -380:
        score.p2_scores()
        time.sleep(2)
        t = 0.1
        ball.reset_pos()

    if score.p1_score == max_score or score.p2_score == max_score:
        game_is_on = False


screen.exitonclick()
