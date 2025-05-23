import tkinter as tk
import pandas as pd
import random
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
df = data.to_dict(orient='records')
current_card = {}


def right():
    global current_card
    current_card = random.choice(df)
    text = current_card['French']
    flashcard_canvas.itemconfig(word, text=f'{text}')
    flashcard_canvas.itemconfig(title, text=f'french')
    window.after(5000, flip_card)
    remove_card()


def remove_card():
    df.remove(current_card)
    data_frame = pd.DataFrame(df)
    data_frame.to_csv('data/words_to_learn.csv', index=False)




def flip_card():
    text_back = current_card['English']
    flashcard_canvas.itemconfig(word, text=f'{text_back}', fill='white')
    flashcard_canvas.itemconfig(title, text=f'english', fill='white')
    flashcard_canvas.itemconfig(image_canvas, image=back_img)

def wrong():
    global current_card
    current_card = random.choice(df)
    text = current_card['French']
    flashcard_canvas.itemconfig(word, text=f'{text}')
    flashcard_canvas.itemconfig(title, text=f'french')
    window.after(5000, flip_card)
BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flashcard_canvas = tk.Canvas(width=800, height=526, highlightthickness=0)
flashcard_canvas.config(bg=BACKGROUND_COLOR)
front_img = tk.PhotoImage(file="images/card_front.png")
back_img = tk.PhotoImage(file="images/card_back.png")
image_canvas = flashcard_canvas.create_image(400, 263, image=front_img)
word = flashcard_canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, 'bold'))
title = flashcard_canvas.create_text(400, 150, text="title ", font=("Arial", 40, 'italic'), fill="black")
flashcard_canvas.grid(row=1, column=0, columnspan=3)
tick_img = tk.PhotoImage(file="images/right.png")
tick_button = tk.Button(image=tick_img, highlightthickness=0, command=right)
tick_button.grid(row=2, column=0)
cross_img = tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross_img, highlightthickness=0, command=wrong)
cross_button.grid(row=2, column=2)
right()

window.mainloop()
