import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        newx = self.xcor() + self.x
        newy = self.ycor() + self.y
        self.goto(newx, newy)

    def colide(self):
        self.y *= -1

    def bounce(self):
        self.x *= -1

    def reset(self):
        self.goto(0, 0)
        self.x *= -1
        self.y *= -1
        self.move()
