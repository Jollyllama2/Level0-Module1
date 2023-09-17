import math
from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()



    radius = simpledialog.askinteger(title='hi',prompt='whats the radius of a circle')
    circle = simpledialog.askstring(title='hi',prompt='would you like to calculate the area of a circle or the circumference')


    if circle == 'area':
        area = math.pi*radius*radius
        messagebox.showinfo(title='hi',message = ' the area is '+str (area))

    if circle == 'circumference':
        circumference = math.pi
        messagebox.showinfo(title='hi', message=' the circumference is ' +str (circumference))






# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
