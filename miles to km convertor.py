import tkinter
from tkinter import *

BACKGROUND_COLOR = "#637E76"
FONT = ("times new roman", 15, "bold")

window = tkinter.Tk()
window.title("miles to km convertor")
window.minsize(width=300, height=200)
window.config(padx=40, pady=20, bg=BACKGROUND_COLOR)

# 1 mile = 1.609 km
entry = Entry(width=25)
entry.focus()
entry.grid(column=1, row=0)

mile_label = Label(pady=20, padx=20, text="miles", bg=BACKGROUND_COLOR, font=FONT)
mile_label.grid(column=2, row=0)

label1 = Label(text="is equal to ", bg=BACKGROUND_COLOR, font=FONT)
label1.grid(column=0, row=1)

label2 = Label(text="0", bg=BACKGROUND_COLOR, font=FONT)
label2.grid(column=1, row=1)

label3 = Label(text="km", bg=BACKGROUND_COLOR, font=FONT)
label3.grid(column=2, row=1)


def calculate(event):
    kilometer = round(float(entry.get()) * 1.609, 3)
    label2.config(text=f"{kilometer}", fg="#FAEF5D")


calculate_button = Button(padx=10, pady=2, fg="#B80000", text="calculate", width=8, background="#F8FAE5", command=calculate, font=FONT)
calculate_button.grid(column=1, row=2)
entry.bind("<Return>", calculate)

window.mainloop()
