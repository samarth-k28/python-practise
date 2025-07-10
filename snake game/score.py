import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.highscore = 0
        self.color('white')
        self.score = turtle.Turtle
        self.score.hideturtle(self)
        self.score.penup(self)
        self.score.goto(self, x=0, y=280)


    def display_score(self):
        self.score.write(self, arg=f'score={self.points}', align='center', font=('Arial', 20, 'bold'))

    def update_score(self):
        self.score.clear(self)
        self.points += 1
        self.score.write(self, f'score={self.points}', align='center', font=('Arial', 20, 'bold'))
        if self.points > self.highscore:
            self.highscore = self.points

    def game_over(self):
        self.score.goto(self, 0, 0)
        self.score.write(self, 'Game Over', align='center', font=('Arial', 30, 'bold'))
    



