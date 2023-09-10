from datetime import date
from tkinter import messagebox, simpledialog, Tk




if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birthday = simpledialog.askstring(title='hi', prompt='type in your birthday')
    currentday = date.today()
    print(currentday)
    if birthday == currentday:
        messagebox.showinfo(title='hello',message='Happy Birthday')
    else:
        messagebox.showinfo(title='hi',message='Happy UNbirthday')