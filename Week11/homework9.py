from tkinter import *
from tkinter import messagebox as msg

### EVENT HANDLERS ###
def btn_gene_rece_clicked():
    name = str(txt_name.get())
    if not name:
        msg.showerror('Error', 'Please enter your name')
        return
    selected_workshops = []
    if workshop1_checked.get():
        total = 50
        selected_workshops.append('Workshop A - Python Basics')
    if workshop2_checked.get():
        total += 100
        selected_workshops.append('Workshop B - Machine Learning')
    if workshop3_checked.get():
        total += 75
        selected_workshops.append('Workshop C - Web Development')
    if workshop4_checked.get():
        total += 60
        selected_workshops.append('Workshop D - Data Visualization')

    if not selected_workshops:
        msg.showerror('Error', 'Please select at least one workshop')
        return

    text = f'\nReceipt for {name}\n\n'
    text += '\n'.join(selected_workshops)
    text += f'\n\nTotal Fee: ${total}'
    lbl_receipt.config(text=text)

### CREATE WINDOW ###
window = Tk()
window.title('Event Registration')
window.geometry('400x330')

### CREATE WIDGETS ###
lbl_title = Label(window, text='Event Registration Form')
lbl_title.grid(row=1, column=1)

txt_name = Entry(window, width=35)
txt_name.grid(row=2, column=1)

workshop1_checked = BooleanVar()
chk_workshop1 = Checkbutton(window, text='Workshop A - Python Basics ($50)', variable=workshop1_checked)#, \
#                                                                                command=btn_gene_rece_clicked)
chk_workshop1.grid(row=3, column=1, columnspan=2, sticky=W)

workshop2_checked = BooleanVar()
chk_workshop2 = Checkbutton(window, text='Workshop B - Machine Learning ($100)', variable=workshop2_checked)#, \
#                                                                                command=btn_gene_rece_clicked)
chk_workshop2.grid(row=4, column=1, columnspan=2, sticky=W)

workshop3_checked = BooleanVar()
chk_workshop3 = Checkbutton(window, text='Workshop C - Web Development ($75)', variable=workshop3_checked)#, \
#                                                                                command=btn_gene_rece_clicked)
chk_workshop3.grid(row=5, column=1, columnspan=2, sticky=W)

workshop4_checked = BooleanVar()
chk_workshop4 = Checkbutton(window, text='Workshop D - Data Visualization ($60)', variable=workshop4_checked)#, \
#                                                                                command=btn_gene_rece_clicked)
chk_workshop4.grid(row=6, column=1, columnspan=2, sticky=W)

btn_gene_rece = Button(window, text='Generate Receipt', command=btn_gene_rece_clicked)
btn_gene_rece.grid(row=7, column=1)

lbl_receipt = Label(window, text='', justify='left')
lbl_receipt.grid(row=8, column=1, sticky=W)

### START THE GUI ###
window.mainloop()