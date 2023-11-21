import tkinter as Tk
import math
from tkinter import *

import parse


def function1():
    print('fine')


root = Tk()
mymenu = Menu(root)
root.config(menu=mymenu)
root.title('calculator')

submenu = Menu(mymenu)
mymenu.add_cascade(label="calculator Basic", menu=submenu)

submenu.add_command(label="calculator scientific", command=function1)
submenu.add_command(label="currency coverter", command=function1)
submenu.add_separator()
submenu.add_command(label="to be continued", command=function1)


display = Entry(root)
display.grid(row= 1, columnspan=7,sticky=W+E)

i=0
def get(num):
    global i
    display.insert(i,num)
    i+=1

def calc():
    entireSTR = display.get()
    try:
      parsed_expr = parse.expr(entireSTR)
      result = parsed_expr.compile()
      clr()
      display.insert(0,result)
    except Exception:
        clr()
        display.insert(0,"error")

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
    display.insert(i,operator)
    i+=length

def calculate_factorial():
    # Get the number from the input field
    num = int(display.get())
    
    # Calculate the factorial
    result = 1
    for i in range(1, num + 1):
        result *= i
    display.insert(0, "result")
    
def calculate_factorial1():
    try:
        num = int(display.get())
        if num < 0:
            raise ValueError("negative number")
        result = 1
        for i in range(1, num + 1):
            result *= i
        clr()
        display.insert(0, result)
    except ValueError as e:
        clr()
        display.insert(0, str(e))
    except Exception as e:
        clr()
        display.insert(0, "Error")

def clr():
    display.delete(0,END)

def undo():
    entireSTR = display.get()
    if len(entireSTR):
        newSTR = entireSTR[:-1]
        clr()
        display.insert(0,newSTR)
    else:
        clr()
        display.insert(0,"error")



entry1 = Entry(root)

button1 = Button(root, text="7",padx=20,pady=20, font=('Arial', 20), command=lambda :get(7)).grid(row=2, column=1)

button2 = Button(root, text="8",padx=20,pady=20,font=('Arial', 20), command=lambda :get(8) ).grid(row=2, column=2)

button3 = Button(root, text="9",padx=20,pady=20,font=('Arial', 20), command=lambda :get(9) ).grid(row=2, column=3)

button4 = Button(root, text="4",padx=20,pady=20,font=('Arial', 20), command=lambda :get(4)).grid(row=3, column=1)

button5 = Button(root, text="5",padx=20,pady=20,font=('Arial', 20), command=lambda :get(5)).grid(row=3, column=2)

button6 = Button(root, text="6",padx=20,pady=20,font=('Arial', 20), command=lambda :get(6) ).grid(row=3, column=3)

button7 = Button(root, text="1",padx=20,pady=20,font=('Arial', 20),command=lambda :get(1)).grid(row=4, column=1)

button8 = Button(root, text="2",padx=20,pady=20,font=('Arial', 20), command=lambda :get(2)).grid(row=4, column=2)

button9 = Button(root, text="3",padx=20,pady=20,font=('Arial', 20), command=lambda :get(3)).grid(row=4, column=3)

button10 = Button(root, text="0",padx=20,pady=20,font=('Arial', 20), command=lambda :get(0)).grid(row=5, column=2)

button11 = Button(root, text="AC",padx=20,pady=20,font=('Arial', 20), command=lambda :clr()).grid(row=5, column=1)

button12 = Button(root, text="=",padx=20,pady=20,font=('Arial', 20), command=lambda :calculate()).grid(row=5, column=3)

button13 = Button(root, text="+",padx=20,pady=20,font=('Arial', 20), command=lambda :operation("+")).grid(row=2, column=4)

button14 = Button(root, text="-",padx=20,pady=20,font=('Arial', 20), command=lambda :operation("-")).grid(row=3, column=4)

button15 = Button(root, text="*",padx=20,pady=20,font=('Arial', 20), command=lambda :operation("*")).grid(row=4, column=4)

button16 = Button(root, text="/",padx=20,pady=20,font=('Arial', 20),command=lambda :operation("/")).grid(row=5, column=4)

button17 = Button(root, text="exp", padx=20,pady=20,font=('Arial', 20),command=lambda :operation("**")).grid(row=2, column=5)

button18 = Button(root, text="%",padx=20,pady=20,font=('Arial', 20), command=lambda :operation("%")).grid(row=3, column=5)

button19 = Button(root, text="X!",padx=20,pady=20,font=('Arial', 20), command=lambda :calculate_factorial1()).grid(row=4, column=5)

button20 = Button(root, text="(",padx=20,pady=20,font=('Arial', 20), command=lambda :operation("(")).grid(row=5, column=5)

button21 = Button(root, text="undo",padx=20,pady=20, font=('Arial', 20),command=lambda :undo()).grid(row=2, column=6)

button22 = Button(root, text="pi",padx=20,pady=20,font=('Arial', 20), command=lambda :operation("*3.14")).grid(row=3, column=6)

button23 = Button(root, text="a^2",padx=20,pady=20,font=('Arial', 20), command=lambda :operation("**2")).grid(row=4, column=6)

button24 = Button(root, text=")",padx=20,pady=20, font=('Arial', 20),command=lambda :operation(")")).grid(row=5, column=6)




root.mainloop()