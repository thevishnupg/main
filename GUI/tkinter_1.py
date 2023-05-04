from tkinter import *

window =Tk()

window.geometry('200x300')

lab = Label(text='Hello').pack()
en = Entry().pack()
btn = Button(window,text='button').pack()
radio = Radiobutton().pack()
chk = Checkbutton().pack()

window.mainloop()