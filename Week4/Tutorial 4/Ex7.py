# 7. Modify 06bHelloLucky from “L03 Decisions solutions” so that it runs inside a while loop (like
# the Concessions example from the lecture). The code should prompt the user for their name
# before the loop starts and at the end of the loop and the while loop should terminate if the
# user doesn’t enter any input at this prompt.

import random as rd
name = input('Enter your name: ') == False

while not name:

    number = rd.randint(1, 100)
    print('Your lucky number is', number)

    answer = input("Enter your name: ")
    name = answer == ""