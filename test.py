def a():
    number = int(input("How many coffees? "))
    if number <= 0:
        print("Please enter a positive number")
        return
    cost = 0
    type = input("type")
    if type == "Latte":
        cost = 2.0
    elif type == "Cappuchono":
        cost = 2.5
    else:
        cost = 3.0
    cost *= number
    if number > 5: # discount
        cost -= 0.2
    cost *= number
    print("That will be £" + format(cost, ".2f"))

a()