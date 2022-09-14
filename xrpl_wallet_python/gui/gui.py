from tkinter import *

root = Tk()
root.title('XRP Wallet')

# Creating a Label Widget
myLabel = Label(root, text="Username")

# Pack labels on screen
myLabel.pack()

e = Entry(root, width=50)
e.pack()

# onClick funtction
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

# Button
myButton = Button(root, text="Submit", padx=50, command=myClick)
myButton.pack()

# Event Loop
root.mainloop()
