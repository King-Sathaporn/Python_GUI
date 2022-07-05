from cProfile import label
from secrets import choice
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combo Box")

Label(text="Choose a country").grid(row=0, sticky=W)

# Create a Combobox
country_names = ["United States", "Canada", "Australia", "Germany", "France", "Italy", "Switzerland"]
choice = StringVar(value="select a country")
country_combobox = ttk.Combobox(root, values=country_names, textvariable=choice)
country_combobox.grid(row=0, column=1)

def select_country():
    if(country_combobox.get() != "select a country"):
        Label(text=country_combobox.get()).grid(row=1, sticky=W)

def clear_data():
    country_combobox.set("select a country")
    Label(text="").grid(row=1, sticky=W)

Button(text="submit", command=select_country).grid(row=0, column=2)
Button(text="clear", command=clear_data).grid(row=0, column=3)

root.mainloop()