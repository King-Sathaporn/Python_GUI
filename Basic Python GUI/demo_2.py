from tkinter import *
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("My GUI")
root.geometry("500x500")

#create menu bar
myMenu = Menu()
root.config(menu=myMenu)

def newFile():
    newFile = Tk()
    newFile.title("New File")
    newFile.geometry("500x500")

def help():
    tkMessageBox.showinfo("Help", "This is a help window")

def closeFile():
    if tkMessageBox.askokcancel("Close", "Do you want to close this window?"):
        root.destroy()

#add sub menu
mySubMenu = Menu()
mySubMenu.add_command(label="New File", command=newFile)
mySubMenu.add_command(label="Open File")
mySubMenu.add_command(label="Save File")
mySubMenu.add_command(label="Close File", command=closeFile)

#add main menu
myMenu.add_cascade(label="File", menu=mySubMenu)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")
myMenu.add_cascade(label="Help", command=help)


root.mainloop()