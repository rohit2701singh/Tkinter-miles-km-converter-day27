import tkinter
from tkinter import *

window = tkinter.Tk()

# ------------ set the window ------------

window.title("my first GUI program")
window.minsize(width=500, height=300)

# ------------ set the label ----------------

my_label = tkinter.Label(text="I'm a label", font=("times new roman", 15, "bold"))
my_label.pack(side="top")

# ---------------- change the label ----------------

my_label["text"] = "label got changed"
my_label.config(text="again got changed")


# -------------- creating button and adding functionality ----------------
def button_clicked():
    # my_label.config(text="button got clicked")
    # print("i got clicked.")
    my_label.config(text=entry.get())


button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

# ----------------- Entry component ---------------------

entry = tkinter.Entry(width=40)
entry.insert(END, string="some text to begin with.")
print(entry.get())
entry.pack()

# ------------ Text box --------------------

text = Text(height=6, width=35)
text.focus()  # put cursor in textbox
text.insert(END, "Example of multiline text entry.")  # add some text to begin with
print(text.get("1.0", END))  # gets current value in textbox at line 1, character 0
text.pack()


# ----------------- spin box -------------------
def spinbox_used():
    print(4 + int(spinbox.get()))


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# ---------------- scale -------------------
def scale_used(number):
    print(number)


scale = Scale(from_=0, to=100, command=scale_used)
print(scale.get())
scale.pack()


# ---------------- checkbox -----------------
def checkbutton_used():
    print(checked_state.get())  # print 1 when on and 0 when off


checked_state = IntVar()  # get hold to checked state: 0 is off and 1 is on
checkbutton = Checkbutton(text="is on?", variable=checked_state, command=checkbutton_used)
print(checked_state.get())
checkbutton.pack()


# -------------- radiobutton ------------------
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# --------------- list box ------------------
def listbox_used(event):
    selected_item = listbox.get(listbox.curselection())
    print(selected_item)


fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple", "Grapes", "Strawberry", "Watermelon", "Kiwi", "Peach"]

listbox = Listbox(height=10, width=20, border=8, bg='#80f9ad', font=("times new roman", 12, "bold"))

for item in fruits:
    listbox.insert(END, item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()

# we can use place(x,y) or grid(column,row) in place of pack.
