import sys
import random

def gmn(name="Player1") :
    game_count = 0
    player_wins = 0

    def play_gmn() :
        nonlocal name
        nonlocal player_wins

       
        user_input = input(f"\n{ name} Guess which number I'm thinking of 1 or 2 or 3 : \n ")

        if user_input not in ['1', '2', '3']:
            print("Invalid input. Please enter a number between 1 and 3.")
            return play_gmn()

        user_choice = int(user_input)
        computer_input = int(random.choice("123"))

        print(f"\n {name}, you choice: {user_choice}.")
        print(f"{name}, I was thinking about the number {computer_input}. ")

        def decide_winner(user_choice, computer_input):
            nonlocal player_wins
            nonlocal name
            if user_choice == computer_input:
                player_wins += 1
                return f"{name}, you win!"
            else:
                return f"Sorry, {name}, you lose! Better luck next time."

        game_result = decide_winner(user_choice, computer_input)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGames played: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: { player_wins / game_count:.2%}")
        print(f"\nPlay again?, {name}")

        while True:
            play_again = input("\nY for Yes, \nQ to Quit: \n\n")
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break

        if play_again.lower() == 'y':
            return play_gmn()
        else:
            print("Thanks for playing!")
            if __name__ == "__main__":
               sys.exit(f"Bye Bye!, {name}")
            else:
                return  

    return play_gmn


if __name__ == "__main__" :

    import argparse
    
    parser = argparse.ArgumentParser(description="Provide a personalized game experience")
    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="Name of the person playing the game"
    )

    args = parser.parse_args()
    guess_my_number = gmn(args.name)
    guess_my_number()