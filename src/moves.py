HIGHEST_SQUARE = 2 ** 63


def get_white_pawn_moves(board, position: int, side: str) -> list[int]:
    """"""
    moves = []
    if position << 8 <= HIGHEST_SQUARE:
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
            if en_passant_side is not None and en_passant_side != side:
                moves.append(position << 1)
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
            if en_passant_side is not None and en_passant_side != side:
                moves.append(position >> 1)
    if position <= 2 ** 15:
        double_side, double_piece, double_board = board.identify_piece_at(
            position << 16
        )
        if double_side is None or double_side != side:
            moves.append(position << 16)
    return moves
