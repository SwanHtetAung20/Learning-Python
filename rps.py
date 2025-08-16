import sys
import random
from enum import Enum

def play_rps() :

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3


    user_input = input("\nPlease Enter \n 1 for ROCK, \n 2 for PAPER, or \n 3 for SCISSORS: \n ")

    if user_input not in ['1', '2', '3']:
        print("Invalid input. Please enter a number between 1 and 3.")
        return play_rps()

    user_choice = int(user_input)
    computer_input = int(random.choice("123"))

    print('\nYour choice: ' + str(RPS(user_choice)).replace('RPS.', '') + '.\n')
    print('Computer choice: ' + str(RPS(computer_input)).replace('RPS.', '') + '.\n')

    if user_choice == computer_input:
        print('It\'s a tie!')
    elif user_choice == 1 and computer_input == 3:
        print('You win! ROCK beats SCISSORS.')
    elif user_choice == 2 and computer_input == 1:
        print('You win! PAPER beats ROCK.')
    elif user_choice == 3 and computer_input == 2:
        print('You win! SCISSORS beats PAPER.')
    else:
        print('You lose! Better luck next time.')

    print("\nPlay again?")

    while True:
        play_again = input("\nY for Yes, \nQ to Quit: \n\n")
        if play_again.lower() not in ['y', 'q']:
            continue
        else:
            break

    if play_again.lower() == 'y':
        return play_rps()
    else:
        print("Thanks for playing!")
        sys.exit("Bye Bye!") 


play_rps()
    
