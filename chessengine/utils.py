"""
Utility functions for common bitboard operations.
"""


import re
from math import log2


piece_characters = {
    ("white", "kings"): "K",
    ("white", "queens"): "Q",
    ("white", "rooks"): "R",
    ("white", "bishops"): "B",
    ("white", "knights"): "N",
    ("white", "pawns"): "P",
    ("black", "kings"): "k",
    ("black", "queens"): "q",
    ("black", "rooks"): "r",
    ("black", "bishops"): "b",
    ("black", "knights"): "n",
    ("black", "pawns"): "p",
}


def get_bit_positions(bitboard: int) -> list[int]:
    """
    Returns a list of positions in the bitboard which have a 1.
    1001100 returns [100, 1000, 1000000]
    """
    positions = []
    mask = 1
    for i in range(64):
        if bitboard & mask:
            positions.append(mask)
        mask = mask << 1

    return positions


def get_rank(position: int, log: bool = False) -> int:
    """
    Returns the rank of a position. position either has to be a
    power of 2, or log has to be True.
    Returns the rank which is in range [1, 8]
    """
    if not log:
        position = log2(position)
    return int(position / 8) + 1


def get_file(position: int, log: bool = False) -> int:
    """
    Returns the file of a position. position either has to be a
    power of 2, or log has to be True.
    Returns the file which is in range [1, 8]
    """
    if not log:
        position = log2(position)
    return int((position % 8) + 1)


def lsb_pos(board: int) -> int:
    """
    Clears all but the rightmost set bit on the board.
    i.e. - Returns 0000100 for 1010100
    """
    return board & ~(board - 1)


def clear_lines(n: int) -> None:
    """
    Clears the last n lines printed so we can print there again
    """
    LINE_UP = "\033[1A"
    LINE_CLEAR = "\x1b[2K"
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def to_san(move: str) -> str:
    """
    Attempts to translate a move in any input format into
    standard algebraic notation (SAN).
    This is intended as a layer between getting the user input
    and passing it on to the #move_san method in #bitboard.py ,
    in order to not annoy users who are unfamiliar with SAN.
    NOTE: If the user input can also contain other, non-move-
    related instructions (such as ending the game, or asking
    for a take back), you must parse the move for those
    instructions before applying this function.
    """

    def capitalize(match):
        return match[0].upper()

    # Strip off leading move numbers (like 10... h5 -> h5):
    move = re.sub(r"^[1-9][0-9]*\.+ ?", "", move)
    # Strip off starting square and dashes in straight
    # (non-capturing) pawn moves (like e2-e4 -> e4):
    move = re.sub(r"^([a-h])[2-7] ?- ?\1([1-8])", r"\1\2", move)
    # Allow lowercase piece names (like nf3 -> Nf3):
    # For pieces that cannot be confused with file names:
    move = re.sub(r"^[rnqk]", capitalize, move)
    # For bishops, in cases where it cannot be confused with
    # the b pawn (like bg5 -> Bg5):
    move = re.sub(r"^b([d-h][1-8])", r"B\1", move)
    return move
