"""
Utility functions for common bitboard operations.
"""


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
