"""
Utility functions for common bitboard operations.
"""
from chessengine.lookup_tables import piece_square_table


from typing import List
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


def get_bit_positions(bitboard: int) -> List[int]:
    """
    Returns a list of positions in the bitboard which have a 1.
    For e.g. - 1001100 returns [100, 1000, 1000000] (all numbers in binary)

    :param bitboard: A bitboard.
    """
    positions = []
    if bitboard == 0:
        return positions

    _ = ~bitboard + 1
    positions.append(bitboard & _)
    positions += get_bit_positions(bitboard & ~_)
    return positions


def get_rank(position: int, log: bool = False) -> int:
    """
    Returns the rank of a position. position either has to be a
    power of 2, or log has to be True.
    Returns the rank which is in range [1, 8]

    :param position: The position whose rank is to be returned. See :ref:`position_representation`
    :param log: If True, position will not be assumed to be a power of 2, but an index on the
        chess board.

    .. note:
        The following calls are equivalent -
        ``get_rank(2**8, False)``
        ``get_rank(8, True)``
    """
    if not log:
        position = log2(position)
    return int(position / 8) + 1


def get_file(position: int, log: bool = False) -> int:
    """
    Returns the file of a position. position either has to be a
    power of 2, or log has to be True.
    Returns the file which is in range [1, 8]

    :param position: The position whose file is to be returned. See :ref:`position_representation`
    :param log: If True, position will not be assumed to be a power of 2, but an index on the
        chess board.

    .. note:
        The following calls are equivalent -
        ``get_file(2**8, False)``
        ``get_file(8, True)``
    """
    if not log:
        position = log2(position)
    return int((position % 8) + 1)


def lsb_pos(board: int) -> int:
    """
    Clears all but the rightmost set bit on the board.
    i.e. - Returns 0000100 for 1010100

    :param board: A bitboard
    """
    return board & ~(board - 1)


def clear_lines(n: int) -> None:
    """
    Clears the last n lines printed so we can print there again

    :param n: The number of lines to clear
    """
    LINE_UP = "\033[1A"
    LINE_CLEAR = "\x1b[2K"
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def change_turn(side_to_move: str) -> str:
    """
    Returns "black" if ``side_to_move`` is "white", and "white" otherwise.

    :param side_to_move: The current side
    """
    if side_to_move == "white":
        return "black"
    return "white"


def get_input(prompt: str) -> str:
    """
    Simple wrapper for input to allow testing
    """
    return input(prompt).strip()


def score_from_move(
    side: str, piece: str, start: int, end: int, end_piece: str, prev_score: int
) -> int:
    """
    Takes the previous board evaluation, and a move to be made, and returns the new
    board evaluation.

    :param side: The side that is making the move. Should be one of "white" or "black"
    :param piece: The piece that is making the move. Should be one of
        ["kings", "queens", "rooks", "bishops", "knights", "pawns"]
    :param start: The start position of the move. See :ref:`position_representation`
    :param end: The end position of the move. See :ref:`position_representation`
    :param end_piece: The piece that was captured (if any)
    :param prev_score: The previous score/evaluation of the board before the move was made

    :return: The new score/evaluation of the board after the move is made
    """
    # TODO - Doesn't take into account pawn promotions. Add support for pawn promotions
    piece_values = {
        "pawns": 100,
        "rooks": 500,
        "knights": 320,
        "bishops": 330,
        "queens": 900,
        "kings": 20000,
    }
    if side == "white":
        new_score = (
            prev_score
            - piece_square_table[(side, piece)][int(log2(start))]
            + piece_square_table[(side, piece)][int(log2(end))]
        )
    else:
        new_score = (
            prev_score
            + piece_square_table[(side, piece)][int(log2(start))]
            - piece_square_table[(side, piece)][int(log2(end))]
        )
    if end_piece is not None:
        if side == "white":
            # Captured side was black
            new_score += (
                piece_values[end_piece]
                + piece_square_table[("black", end_piece)][int(log2(end))]
            )
        else:
            # Captured side was white
            new_score -= (
                piece_values[end_piece]
                + piece_square_table[("white", end_piece)][int(log2(end))]
            )
    return new_score
