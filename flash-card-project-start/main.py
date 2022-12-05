from tkinter import *
import pandas
from random import choice

current_card = {}
to_learn = {}

try:
    dataframe = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    dataframe = pandas.read_csv("data/english_words.csv")
else:
    to_learn = dataframe.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, fill="black", text="English")
    canvas.itemconfig(card_word, fill="black", text=current_card["English"])
    
    flip_timer = window.after(3000, flip_card)
    
def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, fill="white", text="Polski")
    canvas.itemconfig(card_word, fill="white", text=current_card["Polski"])
    
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")
FONT_BOLD = ("Ariel", 60, "bold")

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title(string="Flashy")

flip_timer = window.after(3000, flip_card)

# ---------------------- Canvas ------------------------- #
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_img = canvas.create_image(400,263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400,150, text="English", justify="center", font=FONT)
card_word = canvas.create_text(400,263, text="Example", justify="center", font=FONT_BOLD)

# ---------------------- Labels ------------------------- #

# --------------------- Buttons ------------------------- #
x_image = PhotoImage(file="images/right.png")
x_button = Button(text="", command=is_known, border=0, image=x_image, highlightthickness=0)
x_button.grid(column=1, row=2)

y_image = PhotoImage(file="images/wrong.png")
y_button = Button(text="", command=next_card, border=0, image=y_image, highlightthickness=0)
y_button.grid(column=0, row=2)

next_card()

window.mainloop()
