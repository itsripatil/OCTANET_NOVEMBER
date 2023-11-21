import tkinter as tk
import math

def factorial(n):
    return math.factorial(n)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate_factorial():
    try:
        value = int(entry.get())
        result = factorial(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Factorial Calculator")

# Create an entry widget for input
entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "=", "/"
]

row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == "=":
        tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 16), command=calculate_factorial).grid(row=row_val, column=col_val)
    elif button_text == "C":
        tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 16), command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 16), command=lambda num=button_text: button_click(num)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1



root.mainloop()