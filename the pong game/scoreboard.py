import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f'score for left player: {self.l_score} score for right player: {self.r_score} ',
                   align='center', font=('Arial', 24, 'bold'))

    def update(self,l_score, r_score):
        self.clear()
        self.write(f'score for left player: {l_score} score for right player: {r_score} ',
                   align='center', font=('Arial', 24, 'bold'))
