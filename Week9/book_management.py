def book_management(books):
    running = True
    total = 0
    while running:
        print_menu()
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                add_book(books)
            elif choice == 2:
                edit_price(books)
            elif choice == 3:
                search_book(books)
            elif choice == 4:
                total = sell_book(books, total)
            elif choice == 5:
                show_total_sales(total)
            elif choice == 6:
                print_all(books)
            elif choice == 7:
                print('Program ends')
                running = False
            else:
                print('Invalid choice, try again!')
        except ValueError as v:
            print("Error", v)

def print_menu():
    print("1. Add a book")
    print("2. Edit a book's price")
    print("3. Search for a book by name")
    print("4. Sell a book")
    print("5. Show total sales")
    print("6. Print all books")
    print("7. Quit")

def add_book(books):
    title = input('Enter new book title: ')
    if title in books:
        print(f'Book {title} already exists.')
        return
    price = float(input('Enter new book price: '))
    books[title] = price
    print(f'Book {title} add successfully.')

def edit_price(books):
    title = input('Enter a book title to edit: ')
    if title not in books:
        print(f'Book {title} is not in dictionary.')
        return
    new_price = float(input('Enter new price: '))
    books[title] = new_price
    print(f'Book {title} updated price to {new_price} successfully.')

def search_book(books):
    name = input("Enter book title: ")
    found = False
    for title, price in books.items():
        if title == name:
            print(f'{title} - {price}')
            found = True
            break
    if not found:
        print(f'Book {name} is not found.')

def sell_book(books, total):
    title = input('Enter book title to sell: ')
    if title not in books:
        print(f'Book {title} is not found.')
    else:
        sold = books.pop(title)
        print(f'Book {title} has been sold.')
        total += sold
    return total

def show_total_sales(total):
    print(f'{total}')

def print_all(books):
    for title, price in books.items():
        print(f'{title} - {price}')

### MAIN PROGRAM ###
books = {'The Great Gatsby': 9.99, 'To Kill a Mockingbird': 7.99, '1984': 8.99, 'The Catcher in the Rye': 6.99}
book_management(books)