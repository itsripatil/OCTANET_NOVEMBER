from tkinter import *

root = Tk()

class Mybuttons:
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="click frame", command=self.printmessage)





root.mainloop()