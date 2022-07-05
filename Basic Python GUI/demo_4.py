from select import select
from tkinter import *
import tkinter.messagebox

from matplotlib.pyplot import show

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def show_message():
    if(selectLanguge.get() == 1):
        tkinter.messagebox.showinfo("Message", "You have selected Python")
    elif(selectLanguge.get() == 2):
        tkinter.messagebox.showinfo("Message", "You have selected JavaScript")
    elif(selectLanguge.get() == 3):
        tkinter.messagebox.showinfo("Message", "You have selected Java")
    elif(selectLanguge.get() == 4):
        tkinter.messagebox.showinfo("Message", "You have selected C#")

#add choice to the list
selectLanguge = IntVar() #variable to store the choice
selectLanguge.set(1) #set the default choice
Radiobutton(text="Python", variable=selectLanguge, value=1, command=show_message).grid(row=0, column=0)
Radiobutton(text="JavaScript", variable=selectLanguge, value=2, command=show_message).grid(row=0, column=1)
Radiobutton(text="Java", variable=selectLanguge, value=3, command=show_message).grid(row=0, column=2)
Radiobutton(text="C#", variable=selectLanguge, value=4, command=show_message).grid(row=0, column=3)

root.mainloop()