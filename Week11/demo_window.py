from tkinter import *
from tkinter import messagebox as msg

#### EVENT HANDLERS ####
def btn_OK_clicked():
    msg.showinfo('Info', 'OK button clicked')

#### CREATE WINDOW ####
window = Tk()
window.title('Hello GUI App')
window.geometry('300x200')

#### CREATE WIDGETS ####
lbl_message = Label(window, text='Hello World')
lbl_message.grid(row=0, column=0)

lbl_message = Label(window, text='Hello Python')
lbl_message.grid(row=1, column=1)

lbl_message = Button(window, text='OK', command=btn_OK_clicked)
lbl_message.grid(row=2, column=2)

#### START THE GUI ####
window.mainloop()