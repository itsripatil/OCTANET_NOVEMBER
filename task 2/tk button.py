from tkinter import *

root = Tk()

def dosomething():
    print("clicked")

button1 = Button(root, text="click here", command=dosomething)
button1.pack()    





root.mainloop()