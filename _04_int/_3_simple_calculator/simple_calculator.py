import math
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    from tkinter import messagebox, simpledialog, Tk
    window.withdraw()

# Write a Python program that asks the user for two numbers.
    num1=simpledialog.askinteger(title='hi',prompt='Please enter a number')
    num2=simpledialog.askinteger(title='hi', prompt='Please enter a number')
#Then ask the user if the would like to add, subtract, multiply, or divide.
    symbols= simpledialog.askstring(title='hi',prompt='Would you like to add, subtract, multiply, or divide ( no capitals)')
# Use if-else statements to provide the desired math operation on the numbers
    if symbols == 'add':
        messagebox.showinfo(title='hi', message='The sum of your numbers is ' + str(num1 + num2))
    if symbols == 'subtract':
        messagebox.showinfo(title='hi', message='The sum of your numbers is ' + str(num1 - num2))
    if symbols == 'multiply':
        messagebox.showinfo(title='hi', message='The sum of your numbers is ' + str(num1 * num2))
    if symbols == 'divide':
        messagebox.showinfo(title='hi', message='The sum of your numbers is ' + str(num1 / num2))
  #and display the result.
#"""