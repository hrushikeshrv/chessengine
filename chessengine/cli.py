import argparse

from chessengine.bitboard import Board


def prompt_player_side():
    return input("Do you want to play white or black (w/b)? - ").lower().strip()


def play(play_with_player: bool):
    player_side = prompt_player_side()
    while not player_side.startswith(("b", "w")):
        print(
            f"You entered an invalid side - {player_side}. Enter b for black and w for white"
        )
        player_side = prompt_player_side()

    if player_side.startswith("b"):
        b = Board("black")
    else:
        b = Board("white")
    b.play()


def update():
    print("Work in progress.")


def main():
    parser = argparse.ArgumentParser(
        prog=__package__, description="A chess engine written in Python."
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="set verbose",
        action="store_true",
        required=False,
    )

    subparsers = parser.add_subparsers(help="Action to perform", dest="action")
    parser_play = subparsers.add_parser("play", help="Start a new game.")
    parser_play.add_argument(
        "--player", help="Play with other player.", required=False, action="store_true"
    )
    parser_update = subparsers.add_parser("update", help="Update something")

    args = parser.parse_args()
    if args.action == "play":
        play(args.player)
    elif args.action == "update":
        update()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
