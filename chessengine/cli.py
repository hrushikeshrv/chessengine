import argparse
import sys
from functools import wraps

from chessengine.bitboard import Board


def handle_error(f):
    @wraps(f)
    def wrapper():
        try:
            f()
        except KeyboardInterrupt as e:
            print(f"\nDetected {e.__class__.__name__} {e}.")
            print("Exit.")
            sys.exit(1)

    return wrapper


def prompt_player_side():
    side = input("Do you want to play white or black (w/b)? - ").lower().strip()
    while not side.startswith(('b', 'w')):
        print(f'You entered an invalid side - {side}. Enter "w" for white or "b" for black')
        side = input("Do you want to play white or black (w/b)? - ").lower().strip()
    return side


def play(play_with_player: bool):
    board = Board("black")
    if play_with_player:
        board.play_pvp()
    else:
        player_side = prompt_player_side()

        if player_side.startswith("w"):
            board = Board("white")
        board.play()


def update():
    print("Work in progress.")


@handle_error
def main():
    parser = argparse.ArgumentParser(
        prog=__package__, description="A chess engine written in Python"
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
        "-p",
        "--player",
        help="Play against another player.",
        required=False,
        action="store_true",
    )
    
    parser_update = subparsers.add_parser("update", help="Update something.")

    args = parser.parse_args()
    if args.action == "play":
        play(args.player)
    elif args.action == "update":
        update()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
