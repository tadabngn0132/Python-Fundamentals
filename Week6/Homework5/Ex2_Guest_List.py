count = int(input("How many guests attending a party: "))
names = []

for i in range(1, count+1):
    name = input("Enter the names of guests attending a party: ")
    names.append(name)

remove = input("Do you want to remove any guests from the list? (yes/no) ")

if remove == 'yes':
    delete = names.remove((input("Enter the name of the guest to remove:")))
else:
    print()
print(names)