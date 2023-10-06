from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Listbox
from tkinter import messagebox as msg

### EVENT HANDLERS ###
def btn_ok_clicked():
    money = str(txt_money.get())
    with open('money.txt', 'a') as f:
        f.write(money + '\n')

def btn_addition_clicked():
    total = 0

    f = open('money.txt', 'r')
    line = f.readline()

    while line != '':
        print(line.strip())
        total += int(line)
        line = f.readline()

    f.close()
    msg.showinfo("Total", f"Total: {total} VND")

### CREATE WINDOW ###
window = Tk()
window.title('Save Money')
window.geometry('200x100')

### CREATE WIDGETS ###
lbl_title = Label(window, text="Saving Money")
lbl_title.grid(row=0, column=1)

lbl_money = Label(window, text="Money:")
lbl_money.grid(row=1, column=0, sticky=W)

txt_money = Entry(window, width=10)
txt_money.grid(row=1, column=1)

lbl_vnd = Label(window, text="VND")
lbl_vnd.grid(row=1, column=2, sticky=W)

btn_ok = Button(window, text="OK", command=btn_ok_clicked)
btn_ok.grid(row=2, column=1)

btn_calculate = Button(window, text="Addition", command=btn_addition_clicked)
btn_calculate.grid(row=3, column=1, sticky=E)

### START THE GUI ###
window.mainloop()