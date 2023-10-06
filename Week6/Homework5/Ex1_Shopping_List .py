list_items = []

enter = True
while enter:
    item = input("Enter items they want to buy at the grocery store: ")
    list_items.append(item)
    enter = item != ""

list_items.pop()

user_choice = input("Which item? (all/[index]): ")

if user_choice == "all":
    print(list_items)
else:
    print(list_items[int(user_choice)])