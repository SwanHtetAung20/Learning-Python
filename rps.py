import sys
import random
from enum import Enum

def rps() :
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps() :

        nonlocal player_wins
        nonlocal computer_wins

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

        print(f"\nYour choice: {str(RPS(user_choice)).replace('RPS.', '')} .")
        print(f"Computer choice: {str(RPS(computer_input)).replace('RPS.', '')} .")

        def decide_winner(user_choice, computer_input):
            nonlocal player_wins
            nonlocal computer_wins
            if user_choice == computer_input:
                return'It\'s a tie!'
            elif user_choice == 1 and computer_input == 3:
                player_wins += 1
                return'You win! ROCK beats SCISSORS.'
            elif user_choice == 2 and computer_input == 1:
                player_wins += 1
                return'You win! PAPER beats ROCK.'
            elif user_choice == 3 and computer_input == 2:
                player_wins += 1
                return'You win! SCISSORS beats PAPER.'
            else:
                computer_wins += 1
                return'You lose! Better luck next time.'
        
        game_result = decide_winner(user_choice, computer_input)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGames played: {game_count}")
        print(f"Player wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
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
    return play_rps       


play = rps()
play()