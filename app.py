# import modules
from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("My ToDo List")
root.geometry("500x500")

# define font
my_font = Font(family="Brush Script MT", size=30)

# create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# create listbox
my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none",
)

my_list.pack(side=LEFT, fill=BOTH)

# create dummy list
stuff = [
    "Walk the dog",
    "Buy Groceries",
    "Take a nap",
    "Learn Tkinter",
    "Rule the world",
]
# add dummy list to listbox
for item in stuff:
    my_list.insert(END, item)

# create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)


root.mainloop()
