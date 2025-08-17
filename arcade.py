import sys
from rps import rps
from guess_my_number import gmn

def play_game(name="Player1"):
    welcome_back = False

    while True:
        if welcome_back == True:
           print("\nWelcome back to the menu.")

        player_choice = input(f"\n{name}, please choose a game to play: \n1. Rock Paper Scissors \n2. Guess My Number \nX. Exit \n\n")


        if player_choice not in ['1', '2', 'x']:
            print("Invalid choice. Please enter 1, 2, or x.")
            return play_game(name)

        welcome_back = True

        if player_choice == '1':
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player_choice == '2':
            guess_my_number = gmn(name)
            guess_my_number()
        else:
            print("Thank you for playing!")
            sys.exit(f"Goodbye, {name}!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Play a game of Rock Paper Scissors or Guess My Number.")
    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="Name of the player"
    )
    args = parser.parse_args()

    play_game(args.name)            