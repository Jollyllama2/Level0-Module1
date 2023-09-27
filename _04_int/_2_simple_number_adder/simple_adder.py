import math
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    from tkinter import messagebox, simpledialog, Tk
    window.withdraw()
# Write a Python program that asks the user for two numbers.
    num1 = simpledialog.askinteger(title='hi',prompt='enter a number.')
    num2 = simpledialog.askinteger(title='hi',prompt='enter another number')
# Display the sum of the two numbers to the user
    messagebox.showinfo(title='hi',message='The sum of your numbers is '+ str (num1 + num2))