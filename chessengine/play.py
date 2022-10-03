from chessengine.bitboard import Board
from chessengine.utils import randomize_choice_of_player

if __name__ == "__main__":
    player_choice = input("Do you want to play with another player or robot (p/r)? - ")
    while not player_choice.lower().strip().startswith(("p", "r")):
        print(
            f"You entered an invalid side - {player_choice}. Enter b for black and w for white"
        )
        player_choice = input("Do you want to play with another player or robot (p/r)? - ")
    if player_choice.lower().strip().startswith("p"):

        random_choice = input("Randomly assign black/white to players (y/n)- ")
        while not random_choice.lower().strip().startswith(("y", "n")):
            print(
                f"You entered an invalid side - {random_choice}. Enter b for black and w for white"
            )
            random_choice = input("Randomly assign black/white to players (y/n)- ")
        if random_choice.lower().strip().startswith("y"):
            choice = randomize_choice_of_player()
            if choice == "white":
                print("Player 1 is White side")
                print("Player 2 is Black side")
                p_1 = "white"
                p_2 = "black"
            else:
                print("Player 1 is Black side")
                print("Player 2 is White side")
                p_1 = "black"
                p_2 = "white"
            b = Board(choice)
            b.play_player(p_1, p_2)
        else:
            player_side = input("Do you want to play white or black (w/b)? - ")
            while not player_side.lower().strip().startswith(("b", "w")):
                print(
                    f"You entered an invalid side - {player_side}. Enter b for black and w for white"
                )
                player_side = input("Do you want to play white or black (w/b)? - ")
            if player_side.lower().strip().startswith("w"):
                print("Player 1 is White side")
                print("Player 2 is Black side")
                p_1 = "white"
                p_2 = "black"
                b = Board("white")
            else:
                print("Player 1 is Black side")
                print("Player 2 is White side")
                p_1 = "black"
                p_2 = "white"
                b = Board("black")
            b.play_player(p_1, p_2)
    else:
        player_side = input("Do you want to play white or black (w/b)? - ")
        while not player_side.lower().strip().startswith(("b", "w")):
            print(
                f"You entered an invalid side - {player_side}. Enter b for black and w for white"
            )
            player_side = input("Do you want to play white or black (w/b)? - ")
        if player_side.lower().strip().startswith("w"):
            b = Board("black")
        else:
            b = Board("white")
        b.play()