from tkinter import *
from tkinter.ttk import Combobox

movie_dict = {'The Matrix': ['Lana Wachowski, Lilly Wachowski', 'Keanu REeves, Laurence Fishburne, Carrie-Anne Moss'], \
                'The Lord of the Rings': ['Peter Jackson', 'Elijah Wood, Ian Mckellen, Orlando Bloom'], \
                'The Dark Night': ['Christopher Nolan', 'Christian Bale, Heath Ledger, Aaron Eckhart'], \
                'Inception': ['Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page'], \
                'Interstellar': ['Christopher Nolan', 'Matthew McConaughey, Anne Hathaway, Jessica Chastain']}

### EVENT HANDLERS ###
def cbb_movies_selected(event):
    # get movie name from combobox
    movie = cbb_movies.get()
    # set movie info from the dictionary
    director = movie_dict[movie][0]
    actor = movie_dict[movie][1]
    lbl_director['text'] = f'Director: {director}'
    lbl_actors['text'] = f'Actor: {actor}'

### CREATE WINDOW ###
window = Tk()
window.title('Demo Combobox')
window.geometry('400x300')

### CREATE WIDGETS ###
lbl_title = Label(window, text='Select your favourite movie:')
lbl_title.grid(row=0, column=0, columnspan=2, sticky=EW)

movie_list = ['The Matrix', 'The Lord of the Rings', 'The Dark Knight', 'Inception', \
                'Interstellar']
cbb_movies = Combobox(window, values=movie_list)
cbb_movies.grid(row=1, column=0, columnspan=2, sticky=W)
cbb_movies.bind('<<ComboboxSelected>>', cbb_movies_selected)

lbl_info = Label(window, text='Movie info: ')
lbl_info.grid(row=2, column=0, sticky=W)

lbl_director = Label(window, text='Director: ')
lbl_director.grid(row=3, column=0, columnspan=2, sticky=W)

lbl_actors = Label(window, text='Actor: ')
lbl_actors.grid(row=4, column=0, sticky=W)

window.mainloop()