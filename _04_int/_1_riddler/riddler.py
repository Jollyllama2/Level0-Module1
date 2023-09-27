
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score=0
 # Write a python program that asks the user a minimum of 3 riddles.
    riddle1 = simpledialog.askstring(title='hello',prompt='what do you call a grandfather clock?')
    if riddle1 == "An old timer":
      score=score+1
      messagebox.showinfo(title='hi',message='You get a point for the clock question')
    else:
        score=score
        messagebox.showinfo(title='hi',message='that is incorrect ')
    riddle2 = simpledialog.askstring(title='hi',prompt='what happens when you throw a blue rock in the red sea??????')
    if riddle2 == 'It gets wet':
        score=score+1
        messagebox.showinfo(title='hi',message='you sayed it gets wet,so you get a point for riddle 2 ')
    else :
        score=score
        messagebox.showinfo(title='hi',message='That is incorrect')
    riddle3 = simpledialog.askstring(title='hi',prompt='what room has no windows')
    if riddle3 == 'A mushroom':
        score = score + 1
        messagebox.showinfo(title='hi', message='You said a mushroom you which means you got riddle 3 right')
    else:
        score = score
        messagebox.showinfo(title='hi', message='that is incorrect')




# You can look at riddles.com if you don't already know any riddles.

 #Collect the response of each riddle from the user and compare their
  #answers to the correct answer.




# Use a variable to keep track of the correctly answered riddles

    messagebox.showinfo(title='hi',message='your score was' + str (score))
#After all the riddles have been asked, tell the user how many they got
 # correct
#"""