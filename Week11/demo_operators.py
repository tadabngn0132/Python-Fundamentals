from tkinter import *
from tkinter import messagebox as msg

### EVENT HANDLERS ###
def btn_add_clicked():
    operator('+')

def btn_subtract_clicked():
    operator('-')

def btn_multiplication_clicked():
    operator('*')

def btn_division_clicked():
    operator('/')

def operator(op):
    a = int(txt_a.get()) # get content of entry txt_a
    b = int(txt_b.get()) # get content of entry txt_b
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b

    # lbl_result.config(text=result) # set text of label lbl_result
    lbl_result['text'] = str(result)

### CREATE WINDOW ###
window = Tk()
window.title('Arithmetic Operators')
window.geometry('300x200')

### CREATE WIDGETS ###
lbl_a = Label(window, text='a = ')
lbl_a.grid(row=0, column=0)

txt_a = Entry(window, width=5)
txt_a.grid(row=0, column=1)

lbl_b = Label(window, text='b = ')
lbl_b.grid(row=1, column=0)

txt_b = Entry(window, width=5)
txt_b.grid(row=1, column=1)

lbl_c = Label(window, text='c = ')
lbl_c.grid(row=2, column=0)

lbl_result = Label(window, text='')
lbl_result.grid(row=2, column=1, sticky=W)

btn_add = Button(window, text='Add', command=btn_add_clicked)
btn_add.grid(row=3, column=1, sticky=W)

btn_subtract = Button(window, text='Subtract', command=btn_subtract_clicked)
btn_subtract.grid(row=3, column=2, sticky=W)

btn_multiplication = Button(window, text='Multiplication', command=btn_multiplication_clicked)
btn_multiplication.grid(row=3, column=3, sticky=W)

btn_division = Button(window, text='Division', command=btn_division_clicked)
btn_division.grid(row=3, column=4, sticky=W)

### START THE GUI ###
window.mainloop()