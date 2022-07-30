from math import log2


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


def get_rank(position: int) -> int:
    """
    Returns the rank of a position. position has to be a power of 2.
    Returns the rank which is in range [1, 8]
    """
    pos = int(log2(position))
    return int(pos / 8) + 1


def get_file(position: int) -> int:
    """
    Returns the file of a position. position has to be a power of 2.
    Returns the file which is in range [1, 8]
    """
    pos = int(log2(position))
    return (pos % 8) + 1


def lsb_pos(board: int) -> int:
    """
    Clears all but the rightmost set bit on the board.
    i.e. - Returns 0000100 for 1010100
    """
    return board & ~(board - 1)