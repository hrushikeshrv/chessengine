from chessengine.bitboard import Board


if __name__ == "__main__":
    play_against = (
        input(
            'Do you want to play against the computer or another player?\nEnter "c" for computer, "p" for player - '
        )
        .strip()
        .lower()
    )
    while play_against not in ["p", "c"]:
        play_against = input(
            'You entered an invalid character. Enter "p" to play against another player, and "c" to play against the computer - '
        )

    if play_against == "c":
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
    elif play_against == "p":
        b = Board("black")
        b.play_pvp()
