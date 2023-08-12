import random
from tkinter import *
from tkinter import Tk, ttk


root = Tk()
root.geometry('350x200')
root.title('Random number generator')
root.configure(bg='black')
root.resizable(height=FALSE, width=FALSE)

def generated():
    try:
        num1 = int(enterminvalue.get())
        num2 = int(entermaxvalue.get())

        newnum = random.randint(num1, num2)

        formatted = "{}".format(newnum)

        result['text'] = formatted

        print(newnum, formatted)
    except ValueError:
        result.config(text='Must be numeric', fg='red', font=('Helveica 16'))

banner = Label(text="Random number generator", height=5, padx=13, pady=30, anchor=CENTER, font=('Impact 18'), bg='black', fg='white')
banner.place(x=25, y=-75)

minvalue = Label(text = "Min", width=4, height=1, pady=0, padx=0, anchor=NW, font=('Helvetica 10 bold'), bg='black', fg='white')
minvalue.place(x=48, y=60)

maxvalue = Label(text = "Max", width=4, height=1, pady=0, padx=0, anchor=NW, font=('Helvetica 10 bold'), bg='black', fg='white')
maxvalue.place(x=260, y=60)

enterminvalue = Entry(width=5, justify=CENTER, font=('Helvetica 12'))
enterminvalue.place(x=38, y=85)

entermaxvalue = Entry(width=5, justify=CENTER, font=('Helvetica 12'))
entermaxvalue.place(x=252, y=85)

result = Label(text = " ", width=16, height=2, anchor=CENTER, font=('Helvetica 15 bold'), relief='solid', bg='white', fg='black')
result.place(x=72, y=140)

button = Button(text="Generate", width=6, padx=5, height=1, bg='white', fg='black', font=('Helvetica 12 bold'), command=generated)
button.place(x=130, y=75)

root.mainloop()