from cProfile import label
from secrets import choice
from select import select
from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")
'''
        N
    NW  |   NE
W-------+-------E  
    SW  |   SE
        S
'''
def show_message():
    choice1 = select_languge1.get()
    choice2 = select_languge2.get()
    choice3 = select_languge3.get()
    choice4 = select_languge4.get()

    if choice1 == 1:
        Label(root, text="You have selected Python").pack(anchor=W)
    if choice2 == 1:
        Label(root, text="You have selected JavaScript").pack(anchor=W)
    if choice3 == 1:
        Label(root, text="You have selected Java").pack(anchor=W)
    if choice4 == 1:
        Label(root, text="You have selected C#").pack(anchor=W)

#create a list of checkbuttons
select_languge1 = BooleanVar()
select_languge2 = BooleanVar()
select_languge3 = BooleanVar()
select_languge4 = BooleanVar()
Checkbutton(text="Python", variable=select_languge1).pack(anchor=W)
Checkbutton(text="JavaScript", variable=select_languge2).pack(anchor=W)
Checkbutton(text="Java", variable=select_languge3).pack(anchor=W)
Checkbutton(text="C#", variable=select_languge4).pack(anchor=W)

Button(text="show", command=show_message).pack(anchor=W)
root.mainloop()