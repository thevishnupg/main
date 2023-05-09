# showinfo(): Show some relevant information to the user.
# showwarning(): Display the warning to the user.
# showerror(): Display the error message to the user.
# askquestion(): Ask question and user has to answered in yes or no.
# askokcancel(): Confirm the user’s action regarding some application activity.
# askyesno(): User can answer in yes or no for some action.
# askretrycancel(): Ask the user about doing a particular task again or not.
###############################################################################

from tkinter import *
from tkinter import messagebox

root = Tk()
frame = LabelFrame(root,padx=100,pady=100)
frame.pack(padx=10,pady=10)

def info():
    m = messagebox.showinfo('info','You clicked')
    return m
def warning():
    m = messagebox.showwarning('warning','You clicked')
    return m
def error():
    m = messagebox.showerror('error','You clicked')
    return m
def question():
    m = messagebox.askquestion('question','You clicked')
    return m
def ok_cancel():
    m = messagebox.askokcancel('ok_cancel','You clicked')
    return m
def yes_no():
    m = messagebox.askyesno('yes_no','You clicked')
    return m
def retry_cancel():
    m = messagebox.askretrycancel('retry_cancel','You clicked')
    return m

btn1=Button(frame,text='click',command=info,bd=3,fg='black',bg='violet').grid(row=0,column=0,columnspan=2,padx=10,pady=10)
btn2=Button(frame,text='click',command=warning,bd=3,fg='black',bg='indigo').grid(row=0,column=2,columnspan=2,padx=10,pady=10)
btn3=Button(frame,text='click',command=error,bd=3,fg='black',bg='blue').grid(row=0,column=4,columnspan=2,padx=10,pady=10)
btn4=Button(frame,text='click',command=question,bd=3,fg='black',bg='green').grid(row=1,column=0,columnspan=2,padx=10,pady=10)
btn5=Button(frame,text='click',command=ok_cancel,bd=3,fg='black',bg='yellow').grid(row=1,column=2,columnspan=2,padx=10,pady=10)
btn6=Button(frame,text='click',command=yes_no,bd=3,fg='black',bg='orange').grid(row=1,column=4,columnspan=2,padx=10,pady=10)
btn7=Button(frame,text='click',command=retry_cancel,bd=3,fg='black',bg='red').grid(row=2,column=2,columnspan=2,padx=10,pady=10)


root.mainloop()