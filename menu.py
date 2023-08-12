import customtkinter
from tkinter import *
import os

#Basic blocks of the GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.title('Tool Selection')
root.geometry('300x300')
root.resizable(height=FALSE, width=FALSE)

my_font1 = customtkinter.CTkFont("helvetica", 18, 'bold')
my_font2 = customtkinter.CTkFont("arial", 38, 'bold')

#the statements called by the buttons
def select_calculator():
    os.system('calculator.py')

def select_converted():
    os.system('currency.py')

def select_rgen():
    os.system('rgen.py')


#GUI components
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Menu", font=my_font1)
label.pack(pady=12, padx=10)


#buttons that start the other programs
calcbutton = customtkinter.CTkButton(master=frame, text="Calculator", command=select_calculator, font=my_font1)
calcbutton.pack(pady=15, padx=10)

currbutton = customtkinter.CTkButton(master=frame, text="Dollar Exchange", command=select_converted, font=my_font1)
currbutton.pack(pady=22, padx=10)

randbutton = customtkinter.CTkButton(master=frame, text="R Number Gen", command=select_rgen, font=my_font1)
randbutton.pack(pady=18, padx=10)

root.mainloop()