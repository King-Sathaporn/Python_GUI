from cProfile import label
from tkinter import *

root = Tk() # Create a window (widget)
root.title("My GUI") # Set the title of the window
root.geometry("500x500") # Set the size of the window (width x height + x + y)



#create function
def showMessage():
    Label(root, text="Hello World").pack()

def showMessageFromEntry():
    message = txt.get()
    Label(root, text=message).pack()

def openWindow():
    myWindow = Tk()
    myWindow.title("Response")
    myWindow.geometry("500x300")
# Create a label

myLabel1 = Label(root, text="Hello World", fg="white", font=20, bg="black").pack() # Pack is set center of the window
#myLabel2 = Label(root, text="Hello World", fg="red", font=50, bg="yellow").place(x=100, y=100) #place is set the position of the 

'''
myLabel1 = Label(root, text="Hello World", fg="white", font=10, bg="black").grid(row=0, column=0) #grid is set the position of the label
myLabel2 = Label(root, text="Python", fg="red", font=20, bg="yellow").grid(row=0, column=3)
myLabel3 = Label(root, text="Tk GUI", fg="green", font=30, bg="blue").grid(row=1, column=2)
'''
#Entry box
txt = StringVar()
myText = Entry(root, textvariable=txt).pack() 

#Button
myButton1 = Button(root, text="Click Me", bg="red", fg="white", command=showMessage).pack()
myButton2 = Button(root, text="Click Me", command=showMessageFromEntry).pack()
myButton3 = Button(root, text="Open Window", command=openWindow).pack()


root.mainloop() # Start the event loop