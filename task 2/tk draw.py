from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0, 0,100,100)
otherline = canvas.create_line(13,24,105,120, fill="green")

root.mainloop()