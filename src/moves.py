from math import log2
from .lookup_tables import get_rank, get_file, mask_file, mask_rank, lsb_pos

HIGHEST_SQUARE = 2**63


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

    def is_valid_position(pos: int) -> tuple[bool, bool]:
        """
        Returns a tuple(bool). The first value indicates whether
        this position is valid, the second indicates whether the
        loop should break now
        """
        if pos > HIGHEST_SQUARE:
            return False, True
        if pos <= 0:
            return False, True
        if pos & board.all_pieces == 0:
            return True, False
        elif pos & board.all_white == 0:
            return True, True
        else:
            return False, True

    _ = position
    while True:
        # Move forward
        _ = _ << 8
        valid, should_break = is_valid_position(_)
        if valid:
            moves.append(_)
        if should_break:
            break

    _ = position
    while True:
        # Move backward
        _ = _ >> 8
        valid, should_break = is_valid_position(_)
        if valid:
            moves.append(_)
        if should_break:
            break

    file = get_file(position)
    max_right = 8 - file
    _ = position
    for i in range(max_right):
        # Move right
        _ = _ << 1
        valid, should_break = is_valid_position(_)
        if valid:
            moves.append(_)
        if should_break:
            break

    max_left = file - 1
    _ = position
    for i in range(max_left):
        # Move left
        _ = _ >> 1
        valid, should_break = is_valid_position(_)
        if valid:
            moves.append(_)
        if should_break:
            break
    
    for move in moves:
        print(log2(move))
    return moves
