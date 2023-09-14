from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox

window_width = 600
window_height = 600
if __name__ == '__main__':
    window = Tk()
root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
choices = messagebox.showinfo(title='hi',message='You have three choic es; green red and yellow')
tomato = simpledialog.askstring(title='hi', prompt="what color tomato would you like")


#    You can give them up to three choices

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
canvas.create_oval(95, 200, 500, 450, fill="red", outline="")
canvas.create_oval(600, 260, 525, 450, fill="yellow", outline="")

canvas.create_rectangle(25, 950, 35, 30, fill="green", outline="")

root.mainloop()
