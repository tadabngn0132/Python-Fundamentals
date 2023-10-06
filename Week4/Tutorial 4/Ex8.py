# 8. [Quite hard] Can you modify 08Concessions_whileLoop so that there is only one line of code
# which prompts the user for their name?
name = ""

while name == "":
    
    name = input("What is your name? ")

    if name == "":
        print()
    else:
        student_str = input("Are you a student [y/n]? ")
        student = student_str.lower() in ("y", "yes")

        age_str = input("How old are you? ")
        age = int(age_str)

        message = f"Hello {name}"

        if student and (age <= 18 or age > 65):
            message += " - congratulations, you are entitled to a 20% discount"
        elif student or (age <= 18 or age > 65):
            message += " - congratulations, you are entitled to a 10% discount"
        else:
            message += " - sorry, you must pay the regular price"

        print(message)
        print()

print()
input("Press return to continue ...")