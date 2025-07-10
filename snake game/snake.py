import turtle

y_axis = [-20, 0, 20]
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]
        self.a = 0

    def creat_snake(self):
        for index in range(0, 3):
            self.a = y_axis[index]
            self.add_segments(x=self.a, y=0)

    def add_segments(self, x, y):
        tim = turtle.Turtle()
        tim.speed(1)
        tim.penup()
        tim.shape('square')
        tim.fillcolor('white')
        tim.goto(x, y)
        self.segments.append(tim)

    def extend(self):
        self.add_segments(x=self.segments[-1].xcor(), y=self.segments[-1].ycor())

    def move(self):
        for num_segments in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num_segments - 1].xcor()
            new_y = self.segments[num_segments - 1].ycor()
            self.segments[num_segments].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.segments[0].setheading(left)
