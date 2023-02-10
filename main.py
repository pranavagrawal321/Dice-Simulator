import time
import tkinter as tk
from tkinter import messagebox
import random


def roll_dice():
    roll_animation()
    values = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    dice_value = random.choice(values)
    result_label.config(text=str(dice_value))
    value_button.config(text=str(values.index(dice_value) + 1))
    roll_button.config(state="normal")
    root.update()


def roll_animation():
    for i in range(5):
        dice_value = random.choice(["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"])
        result_label.config(text=str(dice_value))
        value_button.config(text="Rolling...")
        roll_button.config(state="disabled")
        root.update()
        time.sleep(0.2)


root = tk.Tk()
root.title("Dice Simulator")
root.resizable(False, False)

name_label = tk.Label(root, text="Dice Simulator", font=("Helvetica", 20, "bold"))
name_label.pack(padx=5, pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 50))
result_label.pack()

value_button = tk.Label(root, text="", font=("Helvetica", 20))
value_button.pack()

roll_button = tk.Button(root, text="Roll the Dice", command=roll_dice)
roll_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=lambda: messagebox.askyesno("Exit", "Do you want to exit ?",
                                                                               parent=root) and root.destroy())
exit_button.pack(pady=5)

root.mainloop()
