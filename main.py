from tkinter import *
from tkinter import messagebox
from random import randrange


def dicevalue():
    button1["text"] = "Next"
    label1 = Label(root, text=randrange(1, 7))
    label1.grid(row=0, column=2)


def exit():
    msg = messagebox.askyesno("Exit", "Do you want to exit ?")
    if msg:
        root.destroy()


root = Tk()
root.title("Dice Simulator")
button1 = Button(root, text="Start", command=dicevalue)
button1.grid(row=1, column=1)
button2 = Button(root, text="Exit", command=exit)
button2.grid(row=1, column=3)
root.mainloop()
