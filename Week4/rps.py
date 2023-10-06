# Game Rock/Sissors/Paper
import random as rd

playing = True

while playing:
    # ask user to choose rock, sissors or paper
    choice = input("Enter your choice (rock, scissors or paper): ")

    # if invalid input
    if choice not in ['rock', 'scissors', 'paper']:
        # print error message
        print("Error message!")
    # else
    else:
        # generate random number for computer ( 1 - rock, 2 - scissors, 3 - paper)

        against = rd.randint(1,4)
        # if against == 1:
        #     against = 'rock'
        # elif against == 2:
        #     against = 'paper'
        # else:
        #     against = 'scissors'

        against = 'rock' if against == 1 else 'scissors' if against == 2 else 'paper'
        
        print("Computer choice:", against)

        # compare user input and computer number to decide a winner

        if choice == against:
            print('Equal')
        elif (choice == 'rock' and against == 3) or (choice == 'paper' and against == 1) or (choice == 'scissors' and against == 2):
            print("Win")
        else:
            print("Lose")

        # ask user if he/she wants to play again

        answer = input("Do you want to play again (y/n): ")

        # if yes, continue the game, otherwise quit the game by setting playing to False
        
        # if answer == "y":
        #     not playing
        # else:
        #     playing

        playing = answer == "y"