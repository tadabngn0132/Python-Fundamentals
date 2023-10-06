# Exercise 1:
age = int(input("Enter your age: "))
print()

if age < 18:
    print("You are not eligible to apply for a driver's license.")
    print()
else:
    print("You are eligible to apply for a driver's license.")
    print()
    if age >= 21:
        print("You are also eligible to rent a car.")
        print()
    else:
        print("You need to be at least 21 years old to rent a car.")
        print()