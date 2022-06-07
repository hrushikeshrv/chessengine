from .lookup_tables import clear_rank, mask_rank, clear_file, mask_file


class Board:
    """
    A class representing a bitboard representation of the chess board
    """

    def __init__(self, side):
        self.white_pawns = 65280  # 1111111100000000 in binary (A2 to H2)
        self.white_rooks = 129  # 10000001 in binary (A1 and H1)
        self.white_knights = 66  # 01000010 in binary (B1 and G1)
        self.white_bishops = 36  # 00100100 in binary (C1 and F1)
        self.white_queen = 16  # 00010000 in binary (D1)
        self.white_king = 8  # 00001000 in binary (E1)
        # TODO - Fill in these positions
        self.black_pawns = 0  # (A7 to H7)
        self.black_rooks = 0  # (A8 and H8)
        self.black_knights = 0  # (B8 and G8)
        self.black_bishops = 0  # (C8 and F8)
        self.black_queen = 0  # (D8)
        self.black_king = 0  # (E8)

        self.all_white = (
            self.white_pawns
            | self.white_rooks
            | self.white_knights
            | self.white_bishops
            | self.white_queen
            | self.white_king
        )

        self.all_black = (
            self.black_pawns
            | self.black_rooks
            | self.black_knights
            | self.black_bishops
            | self.black_queen
            | self.black_king
        )

        self.all_pieces = self.all_black | self.all_white
        self.side = side.lower().strip()

    def identify_valid_moves(self):
        """
        Generator that identifies all valid moves for all pieces on the board on
        the computer's side and yields Board objects for each move
        """

    def get_self_piece_bitboard(self, piece: str):
        """
        Returns the attribute corresponding to the passed piece, considering the board's
        own side. i.e. - If the board is white, calling with piece = 'king' will return
        white king, etc.
        piece can be one of - "king", "queen", "bishop", "knight", "rook", "pawn"
        """
        piece = piece.lower().strip()
        if piece not in {
            "king",
            "queen",
            "bishop",
            "knight",
            "rook",
            "pawn",
        }:
            raise ValueError(
                f"get_self_piece_bitboard got unknown piece.\nExpected one of {{'king', 'queen', 'bishop', 'knight', "
                f"'rook', 'pawn'}}, got {piece} instead."
            )
        
        if self.side == 'white':
            if piece == 'pawn':
                return self.white_pawns
            if piece == 'queen':
                return self.white_queen
            if piece == 'bishop':
                return self.white_bishops
            if piece == 'knight':
                return self.white_knights
            if piece == 'rook':
                return self.white_rooks
            return self.white_king
        else:
            if piece == 'pawn':
                return self.black_pawns
            if piece == 'queen':
                return self.black_queen
            if piece == 'bishop':
                return self.black_bishops
            if piece == 'knight':
                return self.black_knights
            if piece == 'rook':
                return self.black_rooks
            return self.black_king

    def get_piece_bitboard(self, side: str, piece: str):
        """
        Similar to get_self_piece_bitboard, but can be used to get bitboard of any piece
        for any side. Returns the bitboard of the passed side for the passed pieces.
        """
        piece = piece.lower().strip()
        if piece not in {
            "king",
            "queen",
            "bishop",
            "knight",
            "rook",
            "pawn",
        }:
            raise ValueError(
                f"get_piece_bitboard got unknown piece.\nExpected one of {{'king', 'queen', 'bishop', 'knight', "
                f"'rook', 'pawn'}}, got {piece} instead."
            )
        if side not in {"black", "white"}:
            raise ValueError(
                f"get_piece_bitboard got unknown piece.\nExpected one of {{'white', 'black'}}, "
                f"got {side} instead."
            )
        attrname = side + '_' + piece
        if piece not in {"king", "queen"}:
            attrname += 's'
        return getattr(self, attrname)

    def move(self, start: int, to: int, piece_bitboard=None):
        """
        
        """
