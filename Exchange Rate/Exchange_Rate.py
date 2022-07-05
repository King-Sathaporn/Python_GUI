from cProfile import label
from locale import currency
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Exchange Rate")

amout = DoubleVar()
Label(root, text="amout (THB)", padx=10, font=30).grid(row=0, column=0, sticky=W)
et1 = Entry(root, width=30, font=30, textvariable=amout)
et1.grid(row=0, column=1, sticky=W)

coice = StringVar(value="select currency")
Label(root, text="currency", padx=10, font=30).grid(row=1, column=0, sticky=W)
combo = ttk.Combobox(root, width=30, font=30, textvariable=coice)
combo["value"]=("USD", "JPY", "EUR", "GBP")
combo.grid(row=1, column=1)

Label(root, text="result", padx=10, font=30).grid(row=2, column=0, sticky=W)
et2 = Entry(root, width=30, font=30)
et2.grid(row=2, column=1)

def calculate():
    et2.delete(0, END)
    money = amout.get()
    currency = coice.get()
    if currency == "USD":
        result = money * 0.031
    elif currency == "JPY":
        result = money * 3.486
    elif currency == "EUR":
        result = money * 0.026
    elif currency == "GBP":
        result = money * 0.023
    else:
        result = "error"
    et2.insert(0, result)
    
def clear_data():
    et1.delete(0, END)
    et2.delete(0, END)
    combo.set("select currency")


Button(root, text="calculate", font=30, width=15, command=calculate).grid(row=3, column=1, sticky=W)
Button(root, text="clear", font=30, width=15, command=clear_data).grid(row=3, column=1, sticky=E)

root.mainloop()