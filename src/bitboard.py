from .lookup_tables import mask_position, clear_position


class Board:
    """
    A class representing a bitboard representation of the chess board
    """

    def __init__(self, side: str):
        self.white_pawns = 65280  # (A2 to H2)
        self.white_rooks = 129  # (A1 and H1)
        self.white_knights = 66  # (B1 and G1)
        self.white_bishops = 36  # (C1 and F1)
        self.white_queens = 16  # (D1)
        self.white_kings = 8  # (E1)

        self.black_pawns = 71776119061217280  # (A7 to H7)
        self.black_rooks = 9295429630892703744  # (A8 and H8)
        self.black_knights = 4755801206503243776  # (B8 and G8)
        self.black_bishops = 2594073385365405696  # (C8 and F8)
        self.black_queens = 576460752303423488  # (D8)
        self.black_kings = 1152921504606846976  # (E8)

        self.all_white = (
            self.white_pawns
            | self.white_rooks
            | self.white_knights
            | self.white_bishops
            | self.white_queens
            | self.white_kings
        )

        self.all_black = (
            self.black_pawns
            | self.black_rooks
            | self.black_knights
            | self.black_bishops
            | self.black_queens
            | self.black_kings
        )

        self.all_pieces = self.all_black | self.all_white
        
        if side.lower().strip() not in ['black', 'white']:
            raise ValueError(f"side must be one of \"black\" or \"white\". Got {side}")
        self.side = side.lower().strip()

        # A dictionary matching a side and piece to its corresponding bit board.
        # Useful when we want to iterate through all of the bitboards of the board.
        self.boards_table = {
            ("white", "kings"): self.white_kings,
            ("white", "queens"): self.white_queens,
            ("white", "rooks"): self.white_rooks,
            ("white", "bishops"): self.white_bishops,
            ("white", "knights"): self.white_knights,
            ("white", "pawns"): self.white_pawns,
            ("black", "kings"): self.black_kings,
            ("black", "queens"): self.black_queens,
            ("black", "rooks"): self.black_rooks,
            ("black", "bishops"): self.black_bishops,
            ("black", "knights"): self.black_knights,
            ("black", "pawns"): self.black_pawns,
        }

    def get_piece_bitboard(self, side: str, piece: str) -> int:
        """
        Returns the bitboard of the passed side for the passed pieces.
        Calling with side="black" and piece="king" will return the black_kings bitboard, and so on.
        """
        if piece not in {
            "kings",
            "queens",
            "bishops",
            "knights",
            "rooks",
            "pawns",
        }:
            raise ValueError(
                f"get_piece_bitboard got unknown piece.\nExpected one of {{'kings', 'queens', 'bishops', 'knights', "
                f"'rooks', 'pawns'}}, got {piece} instead."
            )
        if side not in {"black", "white"}:
            raise ValueError(
                f"get_piece_bitboard got unknown piece.\nExpected one of {{'white', 'black'}}, "
                f"got {side} instead."
            )
        attrname = side + "_" + piece
        return getattr(self, attrname)

    def get_self_piece_bitboard(self, piece: str) -> int:
        """
        Returns the attribute corresponding to the passed piece, considering the board's
        own side. i.e. - If the board is white, calling with piece='king' will return
        white king, etc.
        piece can be one of - "kings", "queens", "bishops", "knights", "rooks", "pawns"
        """
        return self.get_piece_bitboard(side=self.side, piece=piece)

    def set_piece_bitboard(self, side: str, piece: str, board: int) -> None:
        """
        
        """
        if piece not in {
            "kings",
            "queens",
            "bishops",
            "knights",
            "rooks",
            "pawns",
        }:
            raise ValueError(
                f"get_piece_bitboard got unknown piece.\nExpected one of {{'kings', 'queens', 'bishops', 'knights', "
                f"'rooks', 'pawns'}}, got {piece} instead."
            )
        if side not in {"black", "white"}:
            raise ValueError(
                f"get_piece_bitboard got unknown piece.\nExpected one of {{'white', 'black'}}, "
                f"got {side} instead."
            )
        attrname = side + "_" + piece
        setattr(self, attrname, board)

    def identify_piece_at(self, position: int) -> tuple:
        mask = mask_position[position]
        for side, piece in self.boards_table:
            board = self.boards_table[(side, piece)]
            if board & mask > 0:
                return side, piece, board
        return None, None, None

    def move(self, start: int, end: int) -> None:
        """
        Moves the piece at start to end. Doesn't check if it is currently the correct
        side's turn when it identifies and moves a piece.
        """
        start_side, start_piece, start_board = self.identify_piece_at(start)
        if start_side is None:
            raise ValueError(f"There is no piece at position {start} to move")
        end_side, end_piece, end_board = self.identify_piece_at(end)
        if end_side == start_side:
            raise ValueError(
                f"Can't move from {start} to {end}, both positions have {end_side} pieces."
            )
        if end_piece is not None:
            # Clear the captured piece's position (set "end" to 0)
            opp_side_board = self.get_piece_bitboard(end_side, end_piece)
            opp_side_board &= clear_position[end]
            self.set_piece_bitboard(end_side, end_piece, opp_side_board)

        # Clear the moved piece's original position (set "start" to 0)
        move_side_board = self.get_piece_bitboard(start_side, start_piece)
        move_side_board &= clear_position[start]

        # Set the moved piece's final position (set "end" to 1)
        move_side_board |= mask_position[end]
        self.set_piece_bitboard(start_side, start_piece, move_side_board)
