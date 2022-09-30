from .bitboard import Board


def prompt_player_side():
    return input("Do you want to play white or black (w/b)? - ").lower().strip()


def main():
    player_side = prompt_player_side()
    while not player_side.startswith(("b", "w")):
        print(
            f"You entered an invalid side - {player_side}. Enter b for black and w for white"
        )
        player_side = prompt_player_side()
    if player_side.startswith("w"):
        b = Board("black")
    else:
        b = Board("white")
    b.play()


if __name__ == "__main__":
    main()
