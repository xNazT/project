import tkinter as tk
from tkinter import *
import math

num = ""


def write(symbol):
    global num
    num += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, num)


def evaluate():
    global num
    print(num)
    try:
        num = str(eval(num))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, num)
    except:
        clear()
        text_result.insert(1.0, "Error")


def clear():
    global num
    num = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("630x650")
root.configure(bg='light blue')
root.resizable(height = FALSE, width = FALSE)
text_result = tk.Text(root, height=4, width=35, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=5)


b1 = tk.Button(root, text="1", command=lambda: write(1), width=5, font=("Arial", 32))
b1.grid(row=2, column=1)
b2 = tk.Button(root, text="2", command=lambda: write(2), width=5, font=("Arial", 32))
b2.grid(row=2, column=2)
b3 = tk.Button(root, text="3", command=lambda: write(3), width=5, font=("Arial", 32))
b3.grid(row=2, column=3)

b4 = tk.Button(root, text="4", command=lambda: write(4), width=5, font=("Arial", 32))
b4.grid(row=3, column=1)
b5 = tk.Button(root, text="5", command=lambda: write(5), width=5, font=("Arial", 32))
b5.grid(row=3, column=2)
b6 = tk.Button(root, text="6", command=lambda: write(6), width=5, font=("Arial", 32))
b6.grid(row=3, column=3)

b7 = tk.Button(root, text="7", command=lambda: write(7), width=5, font=("Arial", 32))
b7.grid(row=4, column=1)
b8 = tk.Button(root, text="8", command=lambda: write(8), width=5, font=("Arial", 32))
b8.grid(row=4, column=2)
b9 = tk.Button(root, text="9", command=lambda: write(9), width=5, font=("Arial", 32))
b9.grid(row=4, column=3)
b0 = tk.Button(root, text="0", command=lambda: write(0), width=5, font=("Arial", 32))
b0.grid(row=5, column=2)

btn_add = tk.Button(root, text="+", command=lambda: write("+"), width=5, font=("Impact", 32), bg='#ab5460', fg='white')
btn_add.grid(row=2, column=4)
btn_subtract = tk.Button(root, text="-", command=lambda: write("-"), width=5, font=("Impact", 32), bg='#ab5460',
                         fg='white')
btn_subtract.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="x", command=lambda: write("*"), width=5, font=("Impact", 32), bg='#ab5460',
                         fg='white')
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="÷", command=lambda: write("/"), width=5, font=("Impact", 32), bg='#ab5460',
                       fg='white')
btn_divide.grid(row=5, column=4)
btn_sqrt = tk.Button(root, text="√ ", command=lambda: write("math.sqrt"), width=5, font=("Impact", 32), bg='#ab5460',
                     fg='white')
btn_sqrt.grid(row=6, column=4)

btn_open = tk.Button(root, text="(", command=lambda: write("("), width=5, font=("Arial", 32))
btn_open.grid(row=5, column=1)
btn_closed = tk.Button(root, text=")", command=lambda: write(")"), width=5, font=("Arial", 32))
btn_closed.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clear, width=5, font=("Impact", 32), bg='#60699f', fg='white')
btn_clear.grid(row=6, column=1)

btn_equals = tk.Button(root, text="=", command=evaluate, width=5, font=("Impact", 32), bg='#60699f',
                       fg='white')
btn_equals.grid(row=6, column=3)

root.title("really cool calculator")
root.mainloop()
