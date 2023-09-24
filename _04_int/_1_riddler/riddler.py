
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
 # Write a python program that asks the user a minimum of 3 riddles.
    riddle1 = simpledialog.askstring(title='hello',prompt='what do you call a grandfather clock?')
    riddle2 = simpledialog.askstring(title='hi',prompt='what happens when you throw a blue rock in the red sea??????')
    riddle3 = simpledialog.askstring(title='hi',prompt='what room has no windows')
# You can look at riddles.com if you don't already know any riddles.

 #Collect the response of each riddle from the user and compare their
  #answers to the correct answer.
    if riddle1 == "an old timer":
      messagebox.showinfo(title='hi',message='You get a point')
    else:
      messagebox.showinfo(title='hi',message='that is incorrect and you get no points')

# Use a variable to keep track of the correctly answered riddles

#After all the riddles have been asked, tell the user how many they got
 # correct
#"""