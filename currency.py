from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk


root = Tk()
root.geometry('300x320')
root.title('Currency Converter')
root.configure(bg='white')
root.resizable(height=FALSE, width=FALSE)


top = Frame(root, width=300, height=60, bg='light green')
top.grid(row=0, column=0)

main = Frame(root, width=300, height=260, bg='white')
main.grid(row=1, column=0)

def convert():
    try:
        global new_amount
        amount = float(value.get())
        currency_2 = box2.get()

        if currency_2 == 'MXN':
            new_amount = amount * 17.01
        elif currency_2 == 'EUR':
            new_amount = amount * 0.91
        elif currency_2 == 'JPY':
            new_amount = amount * 144.91
        elif currency_2 == 'CAD':
            new_amount = amount * 1.34
    except ValueError:
        result.config(text='Enter numeric values', fg='red')


    formatted = "{:,.2f}".format(new_amount)

    result['text'] = formatted


    print(new_amount, formatted)



icon = Image.open('images/icon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
banner = Label(top, image = icon, compound=LEFT, text="Dollar Exchange", height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg='light green', fg='white')
banner.place(x=0, y=0)

result = Label(main, text = " ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Helvetica 15 bold'), bg='white', fg='black')
result.place(x=50, y=10)

currency = ['MXN', 'EUR', 'JPY', 'CAD']

from_label = Label(main, text = "From", width=8, height=1, pady=0, padx=0, relief='flat', anchor=NW, font=('Helvetica 10 bold'), bg='white', fg='black')
from_label.place(x=48, y=90)
box1 = Label(main, width=8, text="USD", justify=CENTER, font=("Helvetica 12 bold"))
box1.place(x=50, y=115)

to_label = Label(main, text = "To", width=8, height=1, pady=0, padx=0, relief='flat', anchor=NW, font=('Helvetica 10 bold'), bg='white', fg='black')
to_label.place(x=158, y=90)
box2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Helvetica 12 bold"))
box2['values'] = (currency)
box2.place(x=160, y=115)


value = Entry(main, width=22, justify=CENTER, font=('Helvetica 12'), relief=SOLID)
value.place(x=50, y=155)

button = Button(main, text="Convert", width=19, padx=5, height=1, bg='light green', fg='white', font=('Helvetica 12 bold'), command=convert)
button.place(x=50, y=210)


root.mainloop()
