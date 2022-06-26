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
    rank = get_rank(position)
    file = get_file(position)

    masked_file = board.all_pieces & mask_file[file]
    lsb = lsb_pos(masked_file)
    while True:
        lsb = lsb << 8
        print(lsb)
        if lsb > HIGHEST_SQUARE:
            break
        if lsb == position:
            continue

        if lsb & board.all_pieces == 0:
            # If there is no piece at the current value of lsb,
            # we can move the piece there
            moves.append(lsb)
        elif lsb & board.all_white == 0:
            moves.append(lsb)
            break
        else:
            break

    masked_rank = board.all_pieces & mask_rank[rank]
    lsb = lsb_pos(masked_rank)
    while True:
        lsb = lsb << 1
        if lsb > HIGHEST_SQUARE:
            break
        if lsb == position:
            continue

        if lsb & board.all_pieces == 0:
            moves.append(lsb)
        elif lsb & board.all_white == 0:
            moves.append(lsb)
            break
        else:
            break

    return moves
