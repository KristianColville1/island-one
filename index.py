"""
Application, Author: Kristian Colville
"""
from tkinter import Button, Tk, messagebox

front = Tk()
front.geometry('600x450')

def pop_up():
    """Pops up a seperate window after clicking button"""
    messagebox.showinfo('Pop up', 'Hi there!')

buttonA = Button(front, text = 'Push me', command = pop_up)
buttonA.place(x= 0, y= 0)

front.mainloop()
