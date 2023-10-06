def book_management():
    names = []
    authors = []
    gernes = []
    publication_years = []
    running = True

    while running:
        print_menu()
        choice = int(input("Enter you choice: "))
        if choice == 1:
            add_book(names, authors, gernes, publication_years)
        elif choice == 2:
            delete_book(names, authors, gernes, publication_years)
        elif choice == 3:
            edit_book(names, authors, gernes, publication_years)
        elif choice == 4:
            search_books_by_gerne(names, authors, gernes, publication_years)
        elif choice == 5:
            print_books_by_publication_year(names, authors, gernes, publication_years)
        elif choice == 6:
            print("Program stops")
            running = False
        else:
            print("Invalid choice, try again!")

def print_menu():
    print("1. Add book")
    print("2. Delete book")
    print("3. Edit book")
    print("4. Search books by gerne")
    print("5. Print books by publication year")
    print("6. Quit")

def add_book(names, authors, gernes, publication_years):
    adding = "yes"
    while adding:
        name = input("Enter book title: ")
        names.append(name)
        author = input("Enter book author: ")
        authors.append(author)
        gerne = input("Enter book gerne: ")
        gernes.append(gerne)
        publication_year = input("Enter book publication year: ")
        publication_years.append(publication_year)
        print(f'Book {name} added')
        answer = input("Do you want to add more books? (yes/no): ")
        adding = answer.lower() == "yes"

def delete_book(names, authors, gernes, publication_years):
    deleting = "yes"
    while deleting:
        name = input("Enter book title: ")
        for i in range(len(names)):
            if names[i] == name:
                names.pop(i)
                authors.pop(i)
                gernes.pop(i)
                publication_years.pop(i)
                print(f'Book {name} deleted')
                return
        answer = input("Do you want to continue to delete any books? (yes/no): ")
        deleting = answer.lower() == "yes"

def edit_book(names, authors, gernes, publication_years):
    editing = "yes"
    found_pos = None

    while editing:
        name = input("Enter book title: ")
        for i in range(len(names)):
            if names[i] == name:
                found_pos = i
        
        if found_pos == None:
            print(f'Book {name} is not in the list')
        else:
            authors[found_pos] = input("Enter new author: ")
            gernes[found_pos] = input("Enter new gerne: ")
            publication_years[found_pos] = input("Enter new publication year: ")
            print(f'Book {name} updated')

        answer = input("Do you want to edit any others? (yes/no): ")
        editing = answer.lower() == "yes"

def search_books_by_gerne(names, authors, gernes, publication_years):
    searching = "yes"
    found_pos = 0

    while searching:
        gerne = input("Enter book gerne: ")
        print(f'Books found under genre "{gerne}":')
        for i in range(len(gernes)):
            if gernes[i] == gerne:
                found_pos = i
                print(f'"{names[found_pos]}" by {authors[found_pos]}, publication year: {publication_years[found_pos]}')
        
        answer = input("Do you want to search any gernes? (yes/no): ")
        searching = answer.lower() == "yes"

def print_books_by_publication_year(names, authors, gernes, publication_years):
    print("Books sorted by publication year: ")
    for i in range(len(publication_years)):
        print(f'"{names[i]}" by {authors[i]} ({publication_years[i]}), gerne: {gernes[i]}')

book_management()