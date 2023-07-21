from tkinter import *
import pandas
import random
# --------------- constants
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
# ----------------------------------
try :
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError :
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else :
    data = pandas.read_csv("data/words_to_learn.csv")
    to_learn=data.to_dict(orient="records")

# ---------- card distribution
def next_card() :
    global current_card,flip_timer
    windows.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(language,text="French",fill="black")
    french_word=current_card['French']
    canvas.itemconfig(world_in_language,text=f"{french_word}",fill="black")
    canvas.itemconfig(canvas_image,image=card_font_image)
    flip_timer=windows.after(3000,func=flip_card)
# -------------- flip the card function

def flip_card():
    canvas.itemconfig(language,text="English",fill="white")
    canvas.itemconfig(world_in_language,text=f"{current_card['English']}",fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)

# ------------ when you know the word
def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

# -------------
windows=Tk()
windows.title("Flashcard Game")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=windows.after(3000,func=flip_card)
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_font_image=PhotoImage(file="images\card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400,263,image=card_font_image)
language=canvas.create_text(400,150,text="Title",font=('Ariel',40,'italic'))
world_in_language=canvas.create_text(400,263,text="word",font=('Ariel',60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

wrong_image=PhotoImage(file="images/wrong.png")
right_image=PhotoImage(file="images/right.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)
right_button=Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)



next_card()





windows.mainloop()
