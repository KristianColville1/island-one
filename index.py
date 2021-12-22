"""
Application, Author: Kristian Colville
"""
from tkinter import Button, Tk, messagebox

main = Tk()
main.geometry('600x450')

def calculate():
    """Pops up a seperate window after clicking button"""
    messagebox.showinfo('Pop up', 'Hi there!')

button1 = Button(main, text = 'result', command = calculate)
button1.place()

main.mainloop()
