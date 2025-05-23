from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for a in question_data:
    c=a['text']
    b=a['answer']
    module = Question(c, b)
    question_bank.append(module)
quiz = QuizBrain(question_bank)
check = quiz.next()
while check is True:
    quiz.nxt_question()








