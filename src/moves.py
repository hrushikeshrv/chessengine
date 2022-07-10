from math import log2
from .lookup_tables import get_file, get_rank

HIGHEST_SQUARE = 2**63


def check_valid_position(
    board, pos: int, moves: list[int], auto_add: bool = True
) -> tuple[bool, bool]:
    """
    Returns a tuple(bool). The first value indicates whether
    this position is valid to move to, the second indicates
    whether this is the last valid position in the direction
    that the piece is currently moving (whether the piece
    should try to explore the next position in the direction
    that is being explored)

    If auto_add is True, adds the position to the moves list
    automatically if the move is valid
    """
    if pos > HIGHEST_SQUARE:
        return False, True
    if pos <= 0:
        return False, True
    if pos & board.all_pieces == 0:
        if auto_add:
            moves.append(pos)
        return True, False
    elif pos & board.all_white == 0:
        if auto_add:
            moves.append(pos)
        return True, True
    else:
        return False, True


def get_white_pawn_moves(
    board, position: int, allow_en_passant: bool = True
) -> list[int]:
    """
    Returns a list of end positions a white pawn starting at position can reach
    """
    moves = []
    side = "white"
    if position << 8 <= HIGHEST_SQUARE:
        target_side, target_piece, target_board = board.identify_piece_at(position << 8)
        if target_side != side:
            moves.append(position << 8)
    if position << 9 <= HIGHEST_SQUARE:
        target_side, target_piece, target_board = board.identify_piece_at(position << 9)
        if target_side != side and target_side is not None:
            moves.append(position << 9)
        if target_side is None:
            (
                en_passant_side,
                en_passant_piece,
                en_passant_board,
            ) = board.identify_piece_at(position << 1)
            if (
                allow_en_passant
                and en_passant_side is not None
                and en_passant_side != side
            ):
                moves.append(position << 9)
    if position << 7 <= HIGHEST_SQUARE:
        target_side, target_piece, target_board = board.identify_piece_at(position << 7)
        if target_side != side and target_side is not None:
            moves.append(position << 7)
        if target_side is None:
            (
                en_passant_side,
                en_passant_piece,
                en_passant_board,
            ) = board.identify_piece_at(position >> 1)
            if (
                allow_en_passant
                and en_passant_side is not None
                and en_passant_side != side
            ):
                moves.append(position << 7)
    if position <= 2**15:
        double_side, double_piece, double_board = board.identify_piece_at(
            position << 16
        )
        _, _, _ = board.identify_piece_at(position << 8)
        if double_side != side and _ is None:
            moves.append(position << 16)
    return moves


def get_white_rook_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a white rook starting at position can reach
    """
    moves = []

    _ = position
    while True:
        # Move forward
        _ = _ << 8
        valid, should_break = check_valid_position(board, _, moves)
        if should_break:
            break

    _ = position
    while True:
        # Move backward
        _ = _ >> 8
        valid, should_break = check_valid_position(board, _, moves)
        if should_break:
            break

    file = get_file(position)
    max_right = 8 - file
    _ = position
    for i in range(max_right):
        # Move right
        _ = _ << 1
        valid, should_break = check_valid_position(board, _, moves)
        if should_break:
            break

    max_left = file - 1
    _ = position
    for i in range(max_left):
        # Move left
        _ = _ >> 1
        valid, should_break = check_valid_position(board, _, moves)
        if should_break:
            break

    return moves


def get_white_bishop_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a white bishop starting at position can reach
    """
    moves = []

    file = get_file(position)
    max_right = 8 - file
    _ = position
    for i in range(max_right):
        _ = _ << 9
        valid, should_break = check_valid_position(board, _, moves)
        if should_break:
            break

    _ = position
    for i in range(max_right):
        _ = _ >> 7
        valid, should_break = check_valid_position(board, _, moves)
        if should_break:
            break

    max_left = file - 1
    _ = position
    for i in range(max_left):
        _ = _ << 7
        valid, should_break = check_valid_position(board, _, moves)
        if should_break:
            break

    _ = position
    for i in range(max_left):
        _ = _ >> 9
        valid, should_break = check_valid_position(board, _, moves)
        if should_break:
            break

    return moves


def get_white_knight_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a white knight starting at position can reach
    """
    moves = []

    rank = get_rank(position)
    file = get_file(position)

    if rank >= 3:
        if file >= 2:
            _ = position >> 17
            check_valid_position(board, _, moves)
        if file <= 7:
            _ = position >> 15
            check_valid_position(board, _, moves)

    if rank >= 2:
        if file >= 3:
            _ = position >> 10
            check_valid_position(board, _, moves)
        if file <= 6:
            _ = position >> 6
            check_valid_position(board, _, moves)

    if rank <= 6:
        if file >= 2:
            _ = position << 15
            check_valid_position(board, _, moves)
        if file <= 7:
            _ = position << 17
            check_valid_position(board, _, moves)

    if rank <= 7:
        if file >= 3:
            _ = position << 6
            check_valid_position(board, _, moves)
        if file <= 6:
            _ = position << 10
            check_valid_position(board, _, moves)

    return moves


def get_white_king_moves(board, position: int) -> list[int]:
    moves = []

    rank = get_rank(position)
    file = get_file(position)

    if rank >= 2:
        _ = position >> 8
        check_valid_position(board, _, moves)

        if file >= 2:
            _ = position >> 9
            check_valid_position(board, _, moves)

        if file <= 7:
            _ = position >> 7
            check_valid_position(board, _, moves)

    if rank <= 7:
        _ = position << 8
        check_valid_position(board, _, moves)

        if file >= 2:
            _ = position << 7
            check_valid_position(board, _, moves)

        if file <= 7:
            _ = position << 9
            check_valid_position(board, _, moves)

    if file >= 2:
        _ = position >> 1
        check_valid_position(board, _, moves)

    if file <= 7:
        _ = position << 1
        check_valid_position(board, _, moves)

    return moves
