# Exercise 2.
income = float(input("Enter your income ($): "))
creditscore = float(input("Enter your credit score: "))

if income > 50000 and creditscore > 700:
    if income > 100000:
        print("You are eligible for a loan with the lowest interest rates.")
    else:
        print("You are eligible for a loan with low interest rates.")
else:
    if income > 30000 and creditscore > 500:
        print("You are eligible for a loan with moderate interest rates.")
    else:
        print("Sorry, you are not eligible for a loan at this time.")