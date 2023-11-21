from tkinter import *

root = Tk()
label = Label(root, text= "Hello world")

label.pack()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="press here", fg="Red")

button2 = Button(otherframe, text="press here", fg="blue")

button1.pack()
button2.pack()

label1 = Label(root,text ="firstName")
label2 = Label(root,text ="lastName")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row =0, column=0)
label2.grid(row= 1, column= 0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()
import tkinter as Tk
from tkinter import *
import math
import parse

# Create the main root window
root = Tk.Tk()
root.title('Calculator')

# Create a function to open a new window
def open_new_window(window_title, window_function):
    global current_window

    if current_window is not None:
        current_window.withdraw()  # Hide the current window

    current_window = Toplevel(root)
    current_window.title(window_title)

    window_function(current_window)  # Call the function for the specific window

# Create a function for each submenu
def calculator_window(window):
    display = Entry(window)
    display.grid(row=1, columnspan=7, sticky=W + E)

    i = 0

    def get(num):
        global i
        display.insert(i, num)
        i += 1

    def calculate():
        try:
            result = eval(display.get())
            clr()
            display.insert(0, str(result))
        except Exception as e:
            clr()
            display.insert(0, "Error")

    def operation(operator):
        global i
        length = len(operator)
        display.insert(i, operator)
        i += length

    def clr():
        display.delete(0, END)

    def undo():
        entireSTR = display.get()
        if len(entireSTR):
            newSTR = entireSTR[:-1]
            clr()
            display.insert(0, newSTR)
        else:
            clr()
            display.insert(0, "error")

    entry1 = Entry(window)

    # Add buttons and logic for this window here

    button1 = Button(window, text="7", padx=20, pady=20, font=('Arial', 20), command=lambda: get(7)).grid(row=2, column=1)
    # Add other buttons similarly...

    window.protocol("WM_DELETE_WINDOW", lambda: close_window(window))

def scientific_calculator_window(window):
    # Create a scientific calculator window here
    pass

def factorial_calculator_window(window):
    # Create a factorial calculator window here
    pass

# Create a menu
menu = Menu(root)
root.config(menu=menu)

# Create a submenu for calculators
calculator_menu = Menu(menu)
menu.add_cascade(label="Calculators", menu=calculator_menu)
calculator_menu.add_command(label="Basic Calculator", command=lambda: open_new_window("Basic Calculator", calculator_window))
calculator_menu.add_command(label="Scientific Calculator", command=lambda: open_new_window("Scientific Calculator", scientific_calculator_window))
calculator_menu.add_command(label="Factorial Calculator", command=lambda: open_new_window("Factorial Calculator", factorial_calculator_window))

# Create a submenu for other options
other_menu = Menu(menu)
menu.add_cascade(label="Other Options", menu=other_menu)
other_menu.add_command(label="Option 1", command=lambda: open_new_window("Option 1", lambda window: print("Option 1 selected")))
other_menu.add_command(label="Option 2", command=lambda: open_new_window("Option 2", lambda window: print("Option 2 selected")))

current_window = None  # Keep track of the current open window

root.mainloop()
