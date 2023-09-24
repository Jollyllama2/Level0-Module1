import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    my_dog = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="hi", prompt= 'what shape do you want to draw, square, circle, of triangle')
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "circle":
        my_dog.circle(radius=124, steps = 30)
    if shape == "square":
        for i in range(4):
            my_dog.right(90)
            my_dog.forward(100)
    if shape == 'triangle':
        for i in range(3):
            my_dog.right(120)
            my_dog.forward(100)

    # Call the turtle .done() method
    turtle.done()