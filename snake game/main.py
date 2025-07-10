import turtle
import time
import snake
import food
import score
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = snake.Snake()
snake.speed = 1
food = food.Food()
score = score.Scoreboard()
score.display_score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game = True
while game is True:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game = False
        score.game_over()
    for segment in snake.segments[1:len(snake.segments)-1:1]:
        if segment == snake.segments[0]:
            pass
        elif snake.head.distance(segment) < 5:
            game = False
            score.game_over()
screen.exitonclick()
