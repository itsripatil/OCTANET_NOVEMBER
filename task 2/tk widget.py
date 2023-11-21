from tkinter import *

root = Tk()

label1 = Label(root, text="First", bg="purple", fg="brown")
label1.pack(fill=X)

label2 = Label(root, text="Second", bg="blue", fg="white")
label2.pack(side=LEFT, fill=Y)
root.mainloop() 
