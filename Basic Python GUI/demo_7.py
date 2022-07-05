from tkinter import *
import math
from turtle import clear

from numpy import arange

root = Tk()
root.title("My GUI")

pi = math.pi
diameter = DoubleVar
area = DoubleVar

Label(text="Diameter", font=30).grid(row=0, sticky=W)
diameter_input = Entry(root, textvariable=diameter, font=30)
diameter_input.grid(row=0, column=1)

Label(text="Area", font=30).grid(row=1, sticky=W)
area_output = Entry(root, font=30)
area_output.grid(row=1, column=1)

def calculate_area():
    if (area_output.get() != ""):
        area_output.delete(0, END)
        
    diameter_value = float(diameter_input.get())
    area = pi *diameter_value**2 / 4
    area_output.insert(0, area)

def clear_data():
    diameter_input.delete(0, END)
    area_output.delete(0, END)

Button(text="Calculate", command=calculate_area).grid(row=2, column=1, sticky=W)
Button(text="Clear", command=clear_data).grid(row=2, column=2, sticky=E)

root.mainloop()