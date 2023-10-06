import pickle

class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

def print_menu():
    print("1. Add book")
    print("2. Delete book")
    print("3. Edit book")
    print("4. Search books by genre")
    print("5. Search books by publication year")
    print("6. Print all books")
    print("7. Save to file")
    print("8. Load from file")
    print("9. Quit")

def add_book(books):
    name = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    publication_year = input("Enter book publication year: ")
    book = Book(name, author, genre, publication_year)
    books.append(book)
    print(f'Book "{name}" added')

def delete_book(books):
    name = input("Enter book title to delete: ")
    found_books = [book for book in books if book.title == name]
    if not found_books:
        print(f'Book "{name}" not found.')
    else:
        for book in found_books:
            books.remove(book)
            print(f'Book "{book.title}" deleted.')

def edit_book(books):
    name = input("Enter book title to edit: ")
    found_books = [book for book in books if book.title == name]
    if not found_books:
        print(f'Book "{name}" not found.')
    else:
        for book in found_books:
            print(f'Editing book "{book.title}":')
            book.author = input("Enter new author: ")
            book.genre = input("Enter new genre: ")
            book.publication_year = input("Enter new publication year: ")
            print(f'Book "{book.title}" updated.')

def search_books_by_genre(books):
    genre = input("Enter book genre to search: ")
    found_books = [book for book in books if book.genre == genre]
    if not found_books:
        print(f'No books found under the genre "{genre}".')
    else:
        print(f'Books found under the genre "{genre}":')
        for book in found_books:
            print(f'"{book.title}" by {book.author}, publication year: {book.publication_year}')

def search_books_by_publication_year(books):
    year = input("Enter publication year to search: ")
    found_books = [book for book in books if book.publication_year == year]
    if not found_books:
        print(f'No books found with publication year "{year}".')
    else:
        print(f'Books published in "{year}":')
        for book in found_books:
            print(f'"{book.title}" by {book.author}, genre: {book.genre}')

def print_all_books(books):
    if not books:
        print("No books in the list.")
    else:
        print("All books:")
        for book in books:
            print(f'"{book.title}" by {book.author}, genre: {book.genre}, publication year: {book.publication_year}')

def save_to_file(books):
    with open('books_data.pkl', 'wb') as file:
        pickle.dump(books, file)
    print("Data saved to file.")

def load_from_file():
    try:
        with open('books_data.pkl', 'rb') as file:
            books = pickle.load(file)
        print("Data loaded from file.")
        return books
    except FileNotFoundError:
        print("No data file found.")
        return []

def main():
    books = load_from_file()

    running = True
    while running:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book(books)
        elif choice == 2:
            delete_book(books)
        elif choice == 3:
            edit_book(books)
        elif choice == 4:
            search_books_by_genre(books)
        elif choice == 5:
            search_books_by_publication_year(books)
        elif choice == 6:
            print_all_books(books)
        elif choice == 7:
            save_to_file(books)
        elif choice == 8:
            books = load_from_file()
        elif choice == 9:
            print("Program stops.")
            running = False
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
