import turtle
import paddel
from ball import Ball
import time
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
r_paddle = paddel.Paddel(370, 0)
l_paddle = paddel.Paddel(x=-370, y=0)
scoreboard = Scoreboard()
l_score= scoreboard.l_score
r_score= scoreboard.r_score
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "w")
screen.onkey(r_paddle.down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.colide()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() > -350):
        ball.bounce()
    elif ball.xcor() > 390:
        ball.reset()
        l_score += 1
        scoreboard.update(l_score,r_score)

    elif ball.xcor() < -390:
        ball.reset()
        r_score += 1
        scoreboard.update(l_score,r_score)
screen.exitonclick()
