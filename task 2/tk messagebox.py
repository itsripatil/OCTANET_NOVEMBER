from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("title","this is message")

responce = tkinter.messagebox.askquestion("question1","do you like coffee")

if responce == 'yes':
    print("here is coffee")


root.mainloop()