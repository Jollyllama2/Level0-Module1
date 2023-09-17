
from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    name=simpledialog.askstring(title='hi',prompt='what is your name')

    if name == 'Luke':
        messagebox.showinfo(title='bruh',message='your amazing at everything')

    if name == 'Asher':
        messagebox.showinfo(title='yo',message='your better than luke at call of duty')

    if name == 'Karina':
        messagebox.showinfo(title='hi',message='you are good at drawing')