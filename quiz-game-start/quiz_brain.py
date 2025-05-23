class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    def next(self):
        if len(self.questions) > self.score:
            return True

        else:
            return False
    def nxt_question(self):
        self.question = self.questions[self.score]
        input(f'Q{self.score+1} {self.question.text}(true/false)?')
        self.score += 1
