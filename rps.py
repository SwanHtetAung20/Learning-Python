import sys
import random
from enum import Enum

def rps(name="Player1") :
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps() :
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        user_input = input(f"\n{ name} Please Enter \n 1 for ROCK, \n 2 for PAPER, or \n 3 for SCISSORS: \n ")

        if user_input not in ['1', '2', '3']:
            print("Invalid input. Please enter a number between 1 and 3.")
            return play_rps()

        user_choice = int(user_input)
        computer_input = int(random.choice("123"))

        print(f"\n {name} choice: {str(RPS(user_choice)).replace('RPS.', '')} .")
        print(f"Computer choice: {str(RPS(computer_input)).replace('RPS.', '')} .")

        def decide_winner(user_choice, computer_input):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal name
            if user_choice == computer_input:
                return f"{name}, it's a tie!"
            elif user_choice == 1 and computer_input == 3:
                player_wins += 1
                return f"{name}, you win! ROCK beats SCISSORS."
            elif user_choice == 2 and computer_input == 1:
                player_wins += 1
                return f"{name}, you win! PAPER beats ROCK."
            elif user_choice == 3 and computer_input == 2:
                player_wins += 1
                return f"{name}, you win! SCISSORS beats PAPER."
            else:
                computer_wins += 1
                return f"Sorry, {name}, you lose! Better luck next time."

        game_result = decide_winner(user_choice, computer_input)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGames played: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
        print(f"\nPlay again?, {name}")

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
            sys.exit(f"Bye Bye!, {name}") 
            
    return play_rps       


if __name__ == "__main__" :

    import argparse
    
    parser = argparse.ArgumentParser(description="Provide a personalized game experience")
    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="Name of the person playing the game"
    )

    args = parser.parse_args()
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()