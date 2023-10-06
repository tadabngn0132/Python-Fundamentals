from tkinter import *
from tkinter import messagebox as msg

### EVENT HANDLERS ###
def btn_calculate_clicked():
    n_night = int(txt_night.get())
    total = n_night * 100
    if breakfast_checked:
        total += n_night * 5
    if late_checked:
        total += 20
    
    lbl_result['text'] = f'${total}'

### CREATE WINDOW ###
window = Tk()
window.title('Room Booking Service')
window.geometry('300x200')

### CREATE WIDGETS ###
lbl_title = Label(window, text='Room Booking Service')
lbl_title.grid(row=0, column=0, columnspan=3, sticky=NE)

lbl_night = Label(window, text='Nights ($100)')
lbl_night.grid(row=1,column=0)

txt_night = Entry(window, width=5)
txt_night.grid(row=1, column=1, columnspan=2, sticky=W)

lbl_extras = Label(window, text='Extras')
lbl_extras.grid(row=2, column=0,sticky=W)

breakfast_checked = BooleanVar()
chk_breakfast = Checkbutton(window, text='Breakfirst ($5)', variable=breakfast_checked)#, \
#                                                            command=btn_calculate_clicked)
chk_breakfast.grid(row=2, column=1, columnspan=2, sticky=W)

late_checked = BooleanVar()
chk_late = Checkbutton(window, text='Late checkout ($20)', variable=late_checked)#, \
#                                                            command=btn_calculate_clicked)
chk_late.grid(row=3, column=1, columnspan=2, sticky=W)

lbl_payment = Label(window, text='Payment')
lbl_payment.grid(row=4, column=0, sticky=W)

lbl_result = Label(window, text='')
lbl_result.grid(row=4, column=1, sticky=W)

btn_calculate = Button(window, text='Enter', command=btn_calculate_clicked)
btn_calculate.grid(row=5, column=1, sticky=W)

### START THE GUI ###
window.mainloop()