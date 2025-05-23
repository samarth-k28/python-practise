# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    count_down(5)


def count_down(count):
    canvas.itemconfig(timer, text=f'{count}')
    if count > 0:
        window.after(10, count, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('pomodoro timer')
window.config(padx=100, pady=100)
window.config(bg=YELLOW)
timer_label = Label(text="Timer", font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
reset_button = Button(text="reset", font=(FONT_NAME, 10, 'bold'), bg=YELLOW)
reset_button.grid(column=2, row=2)
tick_label = Label(text='✔', font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)
image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224)
canvas.create_image(100, 112, image=image)
canvas.config(bg=YELLOW, highlightthickness=0)
timer=canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 30, 'bold'), fill='white')
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 10, 'bold'), bg=YELLOW)
start_button.grid(column=0, row=2)

window.mainloop()
