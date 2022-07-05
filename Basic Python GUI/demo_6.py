from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

Label(text="First Name").grid(row=0, column=0)
Label(text="Last Name").grid(row=0, column=1)
Label(text="Email").grid(row=2, column=0)

input_1 = Entry(root)
input_2 = Entry(root)
input_3 = Entry(root)

input_1.grid(row=1, column=0)
input_2.grid(row=1, column=1)
input_3.grid(row=3, column=0)

input_1.insert(0, "AAAA")
input_2.insert(0, "BBBB")
input_3.insert(0, "123@gmail.com")

def delete_text():
    input_1.delete(0, END)
    input_2.delete(0, END)
    input_3.delete(0, END)

Button(text="Clear", command=delete_text).grid(row=3, column=1)

root.mainloop()