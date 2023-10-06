from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Listbox
from tkinter import messagebox as msg
from books import load_books, load_names

books = load_books()
names = load_names(books)

### EVENT HANDLERS ###
def lst_books_selected(event):
    # get book name from listbox
    book = lst_books.get(lst_books.curselection())
    # set book info from the dictionary
    txt_name.delete(0, END) # clear current
    txt_name.insert(0, book) # insert new text (name of book)
    txt_author.delete(0, END)
    txt_author.insert(0, books[book][0])
    txt_price.delete(0, END)
    txt_price.insert(0, books[book][1])

def btn_OK_clicked():
    price = float(txt_price.get())
    quantity = int(txt_number.get())
    total = price * quantity
    deliver_index = cbb_delivery.current
    # add delivery fee
    if deliver_index == 0: # standard
        total += 1
    elif deliver_index == 1: # fast
        total += 2
    else:
        total += 3
    # add cover fee if selected
    if cover_choice.get() == True:
        total += 2
    msg.showinfo('Total Fee: ', f'Total Fee: ${total}')

def btn_cancel_clicked():
    # clear all texts
    txt_name.delete(0, END)
    txt_author.delete(0, END)
    txt_price.delete(0, END)
    txt_number.delete(0, END)
    cbb_delivery.delete(0, END)

### CREATE WINDOW ###
window = Tk()
window.title('Book Store')
window.geometry('500x400')

### CREATE WIDGETS ###
lbl_books = Label(window, text='Books')
lbl_books.grid(row=0, column=0, sticky=W, padx=10)

lst_books = Listbox(window, height=5, selectmode=SINGLE)
lst_books.grid(row=1, column=0, columnspan=2, rowspan=3, sticky=W, padx=10)
for name in names:
    lst_books.insert(END, name)
lst_books.bind('<<ListboxSelect>>', lst_books_selected)

lbl_name = Label(window, text='Name')
lbl_name.grid(row=1, column=3, sticky=W)

txt_name = Entry(window, width=20)
txt_name.grid(row=1, column=4, columnspan=2, sticky=W)

lbl_author = Label(window, text='Author')
lbl_author.grid(row=2, column=3, sticky=W)

txt_author = Entry(window, width=20)
txt_author.grid(row=2, column=4, columnspan=2, sticky=W)

lbl_price = Label(window, text='Price')
lbl_price.grid(row=3, column=3, sticky=W)

txt_price = Entry(window, width=20)
txt_price.grid(row=3, column=4, columnspan=2, sticky=W)

lbl_number = Label(window, text='Number')
lbl_number.grid(row=4, column=0,sticky=W)

txt_number = Entry(window, width=11)
txt_number.grid(row=4, column=1, sticky=W)

lbl_delivery = Label(window, text='Delivery')
lbl_delivery.grid(row=5, column=0)

cbb_delivery = Combobox(window, width=8)
cbb_delivery['value'] = ('Standard ($1)', 'Fast ($2)', 'Express($5)')
cbb_delivery.grid(row=5, column=1, sticky=W)

lbl_cover = Label(window, text='Cover ($2)')
lbl_cover.grid(row=5, column=3,sticky=W)

cover_choice = IntVar()
rd_cover_yes = Radiobutton(window, text='Yes', value=1, variable=cover_choice)
rd_cover_yes.grid(row=5, column=4, sticky=W)

rd_cover_no = Radiobutton(window, text='No', value=2, variable=cover_choice)
rd_cover_no.grid(row=5, column=5, sticky=W)

btn_ok = Button(window, text='OK', command=btn_OK_clicked)
btn_ok.grid(row=6, column=4, sticky=W)

btn_cancel = Button(window, text='Cancel', command=btn_cancel_clicked)
btn_cancel.grid(row=6, column=5, sticky=W)

### START THE GUI ###
window.mainloop()