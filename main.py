BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

global word_dict
global eng_bg_img
eng_bg_img = None
#----------------------generating words-------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")

def generate_word_right():
    global word_dict,data_dict
    data_dict.remove(word_dict)
    dt = pandas.DataFrame(data_dict)
    dt.to_csv("data/words_to_learn.csv",index=False)
    generate_word_wrong()
def generate_word_wrong():
    global word_dict, break_
    window.after_cancel(break_)
    word_dict = random.choice(data_dict)
    canvas.itemconfig(t,text="French",fill="black")
    words = word_dict["French"]
    canvas.itemconfig(french_words,text=words,fill="black")
    canvas.itemconfig(ff_ww,image=french_bg_img)
    break_ = window.after(3000,eng_word_translation)
def eng_word_translation():
    global eng_bg_img
    global word_dict
    eng_word = word_dict["English"]
    canvas.itemconfig(t, text="English",fill="white")
    canvas.itemconfig(french_words, text=eng_word,fill="white")
    eng_bg_img = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(ff_ww,image=eng_bg_img)



#--------------------------------------UI-----------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)
french_bg_img = PhotoImage(file="images/card_front.png")
ff_ww = canvas.create_image(400, 263, image=french_bg_img)
break_ = window.after(3000,eng_word_translation)
t = canvas.create_text(400,150,text="French",font=("Ariel",30,"italic"))
french_words = canvas.create_text(400,263,text="",font=("Ariel",30,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,bg=BACKGROUND_COLOR,command=generate_word_right)
right_button.grid(row=1,column=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,bg=BACKGROUND_COLOR,command=generate_word_wrong)
wrong_button.grid(row=1,column=1)
generate_word_wrong()








window.mainloop()















