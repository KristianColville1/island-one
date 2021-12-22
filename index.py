from tkinter import *

from tkinter import messagebox

front = Tk()
front.geometry('450x450')

def popUp():
    msg = messagebox.showinfo('Pop up', 'Hi there!')


buttonA = Button(front, text = 'Push me', command = popUp)
buttonA.place(x= 0, y= 0)

front.mainloop()
