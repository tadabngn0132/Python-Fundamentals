def product_management(products):
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_product(products)
        elif choice == 2:
            edit_product(products)
        elif choice == 3:
            delete_product(products)
        elif choice == 4:
            filter_product(products)
        elif choice == 5:
            print_all(products)
        elif choice == 0:
            print('Program ends')
            running = False
        else:
            print('Invalid choice, try again!')

def print_menu():
    print('1. Add product')
    print('2. Edit product')
    print('3. Delete product')
    print('4. Filter product')
    print('5. Print all products')
    print('0. Exit')

def add_product(products):
    name = input('Enter new product name: ')
    if name in products:
        print(f'Product {name} already exists.')
        return
    price = float(input('Enter new product price: '))
    products[name] = price
    print(f'Product {name} add successfully.')

def edit_product(products):
    name = input('Enter a product name to edit: ')
    if name not in products:
        print(f'Product {name} is not in dictionary.')
        return
    new_price = float(input('Enter new price: '))
    products[name] = new_price
    print(f'Product {name} updated price to {new_price} successfully.')

def delete_product(products):
    name = input('Enter product name to delete: ')
    if name not in products:
        print(f'Product {name} not found.')
        return
    del products[name]
    print(f'Product {name} deleted successfully.')

def filter_product(products):
    filter_price = float(input('Enter price to filter: '))
    for name, price in products.items():
        if price >= filter_price:
            print(f'{name} - {price}')
    
    # for name in products:
    #     price = products[name]
    #     if price >= filter_price:
    #         print(f'{name} - {price}')

def print_all(products):
    for name, price in products.items():
        print(f'{name} - {price}')

### MAIN PROGRAM ###
products = {}
product_management(products)