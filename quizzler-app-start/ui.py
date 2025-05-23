THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizzINTERFACE:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.configure(background="#375362", padx=20, pady=20)
        self.score_txt = Label(fg='white', text="Score", bg=THEME_COLOR, font=("Helvetica", 20))
        self.score_txt.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.configure(highlightthickness=0)
        self.canvas.configure(bg='white')
        self.question_txt = self.canvas.create_text(150, 125, width=280, text='question', fill='black',
                                                    font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(row=2, column=1)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.configure(bg='white')
        txt = self.quiz.next_question()
        self.canvas.itemconfig(self.question_txt, text=f'{txt}')

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer('TRUE'))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer('FALSE'))
    def give_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.configure(bg='green')

        else:
            self.canvas.configure(bg='red')
        self.window.after(2000, self.next_question)
        self.score_txt.config(text=f'Score: {self.quiz.score}')
