
from tkinter import *



top = Tk()
top.geometry('140x100')

frame = Frame(top)
frame.pack()

left_frame = Frame(top)
left_frame.pack(side=LEFT)
right_frame = Frame(top)
right_frame.pack(side=RIGHT)


btn1 = Button(frame,text='Submit', fg='red',activebackground='red')
btn1.pack(side=LEFT)


btn2 = Button(frame,text='Submit', fg='green',activebackground='green')
btn2.pack(side=RIGHT)


btn3 = Button(right_frame,text='Submit', fg='blue',activebackground='blue')
btn3.pack(side=LEFT)


btn4 = Button(left_frame,text='Submit', fg='yellow',activebackground='yellow')
btn4.pack(side=RIGHT)



top.mainloop()
