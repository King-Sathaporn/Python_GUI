from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    myLabel = Label(root, text=color[0], bg=color[1]).pack()

#import file and read (text only)
def selectFile():
    file = askopenfilename()
    fileContent = open(file, encoding="utf-8").read()
    myLabel = Label(root, text=fileContent).pack()

btn = Button(root, text="color", command=selectColor).pack()
btn2 = Button(root, text="file", command=selectFile).pack()

root.mainloop()