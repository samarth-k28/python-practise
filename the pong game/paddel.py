import turtle


class Paddel(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def up(self):
        y_axis = self.ycor() + 20
        self.sety(y_axis)

    def down(self):
        y_axis = self.ycor() - 20
        self.sety(y_axis)
