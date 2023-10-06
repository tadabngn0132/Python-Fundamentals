# Enter product information (name, price, stock) and print the information in a table

name = input('Enter product name: ')
price = float(input('Enter product price: '))
stock = int(input('Enter product stock: '))

a = '-'
print(f"+{a*20}+{a*10}+{a*10}+{a*10}+")
print(f'|{"Name":<20}|{"Price":>10}|{"Stock":>10}|{"Value":>10}|')
print(f"+{a*20}+{a*10}+{a*10}+{a*10}+")
print(f'|{name:<20}|{price:>10.2f}|{stock:>10}|{price*stock:>10.2f}|')
print(f"+{a*20}+{a*10}+{a*10}+{a*10}+")