import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True

while play_again:

    user_input = int(input("\nPlease Enter \n 1 for ROCK, \n 2 for PAPER, or \n 3 for SCISSORS: \n "))

    if user_input < 1 or user_input > 3:
        print("Invalid input. Please enter a number between 1 and 3.")
        sys.exit(1)

    computer_input = int(random.choice("123"))

    print('\nYour choice: ' + str(RPS(user_input)).replace('RPS.', '') + '.\n')
    print('Computer choice: ' + str(RPS(computer_input)).replace('RPS.', '') + '.\n')

    if user_input == computer_input:
        print('It\'s a tie!')
    elif user_input == 1 and computer_input == 3:
        print('You win! ROCK beats SCISSORS.')
    elif user_input == 2 and computer_input == 1:
        print('You win! PAPER beats ROCK.')
    elif user_input == 3 and computer_input == 2:
        print('You win! SCISSORS beats PAPER.')
    else:
        print('You lose! Better luck next time.')

    play_again = input("\nPlay again? \nY for Yes, \nN for No or \nQ to Quit: \n\n")   

    if play_again.lower() == 'y':
        continue
    else:
        print("Thanks for playing!")
        play_again = False

sys.exit("Bye Bye!") 
    
