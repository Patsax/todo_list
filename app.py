# import modules
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

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

# entry box to add items to list
my_entry = Entry(root, font=("Freestyle", 24), width=24)
my_entry.pack(pady=20)

# create button frame
button_frame = Frame(root)
button_frame.pack(pady=20)


# functions
def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_off_item():
    # cross off item
    my_list.itemconfig(my_list.curselection(), fg="#dedede")
    # remove selection bar
    my_list.select_clear(0, END)


def uncross_item():
    # uncross item
    my_list.itemconfig(my_list.curselection(), fg="#464646")
    # remove selection bar
    my_list.select_clear(0, END)


def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/gui/data"
    )


def open_list():
    pass


def delete_list():
    my_list.delete(0, END)


# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add selections to menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
# add dropdown items to menu selections
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_list)

# add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
delete_crossed_button = Button(
    button_frame, text="Delete Crossed", command=delete_crossed
)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)


root.mainloop()
