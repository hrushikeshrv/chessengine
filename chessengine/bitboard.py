from copy import copy
from math import log2

from .moves import (
    get_white_pawn_moves,
    get_white_rook_moves,
    get_white_bishop_moves,
    get_white_knight_moves,
    get_white_king_moves,
    get_white_queen_moves,
    get_black_pawn_moves,
    get_black_rook_moves,
    get_black_bishop_moves,
    get_black_knight_moves,
    get_black_king_moves,
    get_black_queen_moves,
)
from .lookup_tables import mask_position, clear_position
from .utils import get_bit_positions, get_rank, get_file


class Board:
    """
    A class implementing a bitboard representation of a chess board
    """

    def __init__(self, side: str):
        self.white_pawns = 65280  # (A2 to H2)
        self.white_rooks = 129  # (A1 and H1)
        self.white_knights = 66  # (B1 and G1)
        self.white_bishops = 36  # (C1 and F1)
        self.white_queens = 8  # (D1)
        self.white_kings = 16  # (E1)

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

        if side.lower().strip() not in ["black", "white"]:
            raise ValueError(f'side must be one of "black" or "white". Got {side}')
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

        # (modified) FEN representation of the board (used to produce a hash string for the board)
        self.FEN = "rnbqkbnr/pppppppp/00000000/00000000/00000000/00000000/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

        # Keep track of all moves made
        self.moves = []

    def __repr__(self):
        piece_list = ["\u2001" for _ in range(64)]
        unicode_piece = {
            ("white", "kings"): "\u2654",
            ("white", "queens"): "\u2655",
            ("white", "rooks"): "\u2656",
            ("white", "bishops"): "\u2657",
            ("white", "knights"): "\u2658",
            ("white", "pawns"): "\u2659",
            ("black", "kings"): "\u265A",
            ("black", "queens"): "\u265B",
            ("black", "rooks"): "\u265C",
            ("black", "bishops"): "\u265D",
            ("black", "knights"): "\u265E",
            ("black", "pawns"): "\u265F",
        }

        def add_bitboard_to_repr(board, s, p):
            board_string = bin(board)[2:]
            board_string = "0" * (64 - len(board_string)) + board_string
            for _ in range(64):
                if board_string[_] == "1":
                    piece_list[_] = unicode_piece[(s, p)]

        for side, piece in self.boards_table:
            add_bitboard_to_repr(self.boards_table[(side, piece)], side, piece)

        board_repr = ""
        for i in range(8):
            board_repr += "\u2001".join(piece_list[8 * i : 8 * i + 8][::-1])
            board_repr += "\n"
        return board_repr

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if self.side != other.side:
            return False

        for side, piece in self.boards_table:
            if self.boards_table[(side, piece)] != other.boards_table[(side, piece)]:
                return False
        return True

    def __hash__(self):
        return hash(self.FEN)

    @property
    def score(self):
        return 0

    @property
    def board_pieces(self):
        if self.side == "white":
            return [
                ("white", "kings"),
                ("white", "queens"),
                ("white", "rooks"),
                ("white", "bishops"),
                ("white", "knights"),
                ("white", "pawns"),
            ]
        return [
            ("black", "kings"),
            ("black", "queens"),
            ("black", "rooks"),
            ("black", "bishops"),
            ("black", "knights"),
            ("black", "pawns"),
        ]

    @property
    def opponent_pieces(self):
        if self.side == "black":
            return [
                ("white", "kings"),
                ("white", "queens"),
                ("white", "rooks"),
                ("white", "bishops"),
                ("white", "knights"),
                ("white", "pawns"),
            ]
        return [
            ("black", "kings"),
            ("black", "queens"),
            ("black", "rooks"),
            ("black", "bishops"),
            ("black", "knights"),
            ("black", "pawns"),
        ]

    def copy(self):
        return copy(self)

    def get_side_bitboard(self, side: str) -> int:
        """
        Returns the bitboard containing all pieces for the given side
        """
        if side == "white":
            return self.all_white
        return self.all_black

    def get_bitboard(self, side: str, piece: str) -> int:
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
                f"get_bitboard got unknown piece.\nExpected one of {{'kings', 'queens', 'bishops', 'knights', "
                f"'rooks', 'pawns'}}, got {piece} instead."
            )
        if side not in {"black", "white"}:
            raise ValueError(
                f"get_bitboard got unknown piece.\nExpected one of {{'white', 'black'}}, "
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
        return self.get_bitboard(side=self.side, piece=piece)

    def update_board_state(self) -> None:
        """
        Updates self.all_white, self.all_black, self.all_pieces, and self.boards_table
        every time a bitboard is updated
        """
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

    def set_bitboard(self, side: str, piece: str, board: int) -> None:
        """
        Sets the bitboard for the passed arguments to the passed bitboard
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
                f"set_bitboard got unknown piece.\nExpected one of {{'kings', 'queens', 'bishops', 'knights', "
                f"'rooks', 'pawns'}}, got {piece} instead."
            )
        if side not in {"black", "white"}:
            raise ValueError(
                f"set_bitboard got unknown piece.\nExpected one of {{'white', 'black'}}, "
                f"got {side} instead."
            )
        attrname = side + "_" + piece
        setattr(self, attrname, board)
        self.update_board_state()

    def identify_piece_at(self, position: int) -> tuple:
        """
        Identifies if there is any piece on the position passed. Returns
        the identified piece, its side, and its board if a piece is found
        at that position, None otherwise.
        """
        # print(bin(self.all_pieces))
        # print(bin(position), log2(position))
        if self.all_pieces & position == 0:
            # If we don't return here, the for loop will definitely return a non-null value
            return None, None, None
        for side, piece in self.boards_table:
            board = self.boards_table[(side, piece)]
            if board & position > 0:
                return side, piece, board

    def move(self, start: int, end: int, track: bool = True) -> None:
        """
        Moves the piece at start to end. Doesn't check anything, just makes
        the move (unless the start or end positions are invalid).
        """
        start_pos = log2(start)
        end_pos = log2(end)
        if not start_pos.is_integer():
            raise ValueError("The start position provided is not a power of 2")
        if not end_pos.is_integer():
            raise ValueError("The end position provided is not a power of 2")

        start_side, start_piece, start_board = self.identify_piece_at(start)
        if start_side is None:
            raise ValueError(f"There is no piece at position {start_pos} to move")

        end_side, end_piece, end_board = self.identify_piece_at(end)
        if end_side == start_side:
            raise ValueError(
                f"Can't move from {start_pos} to {end_pos}, both positions have {end_side} pieces."
            )

        if track:
            # Keep track of the board state before the move was made so we can undo
            start_state = (start, end, end_side, end_piece, end_board)
            self.moves.append(start_state)

        if end_piece is not None:
            # Clear the captured piece's position (set "end" to 0)
            opp_side_board = self.get_bitboard(end_side, end_piece)
            opp_side_board &= clear_position[end_pos]
            self.set_bitboard(end_side, end_piece, opp_side_board)

        # Clear the moved piece's original position (set "start" to 0)
        move_side_board = self.get_bitboard(start_side, start_piece)
        move_side_board &= clear_position[start_pos]

        # Set the moved piece's final position (set "end" to 1)
        move_side_board |= mask_position[end_pos]
        self.set_bitboard(start_side, start_piece, move_side_board)
        self.update_fen_state(
            start_side, start_piece, start_pos, end_side, end_piece, end_pos
        )

    def make_moves(self, *moves: tuple[int]) -> None:
        """
        Given a number of moves as tuples (start, end), call
        Board.move on all
        """
        for start, end in moves:
            self.move(start, end)

    def undo_move(self):
        if not self.moves:
            raise RuntimeError("No moves have been made yet to undo.")
        end, start, side, piece, board = self.moves.pop()
        self.move(start=start, end=end, track=False)

        if side is not None:
            self.set_bitboard(side, piece, board)

    def update_fen_state(
        self, start_side, start_piece, start_position, end_side, end_piece, end_position
    ):
        """
        Updates the FEN representation of the Board
        """
        ranks = self.FEN.split()[0].split('/')
        
        start_rank = get_rank(start_position, log=True)
        start_file = get_file(start_position, log=True)
        start_rank_str = ranks[8-start_rank]
        end_rank = get_rank(end_position, log=True)
        end_file = get_file(end_position, log=True)
        end_rank_str = ranks[8 - end_rank]
        print(start_file, start_rank, end_file, end_rank)
        
        moved_char = start_rank_str[start_file-1]
        if moved_char.isnumeric():
            raise ValueError(f"Board's FEN state is corrupted. - {self.FEN}")
        
        new_rank_str = start_rank_str[:start_file-1] + '0' + start_rank_str[start_file:]
        ranks[8-start_rank] = new_rank_str
        
        new_rank_str = end_rank_str[:end_file-1] + moved_char + end_rank_str[end_file:]
        ranks[8-end_rank] = new_rank_str
        
        self.FEN = '/'.join(ranks) + ' ' + ' '.join(self.FEN.split()[1:])

    def get_moves(self, side: str, piece: str, position: int) -> list[int]:
        """
        Gets all end positions a piece of side can reach starting from position
        """
        move_gens = {
            ("white", "kings"): get_white_king_moves,
            ("white", "queens"): get_white_queen_moves,
            ("white", "rooks"): get_white_rook_moves,
            ("white", "bishops"): get_white_bishop_moves,
            ("white", "knights"): get_white_knight_moves,
            ("white", "pawns"): get_white_pawn_moves,
            ("black", "kings"): get_black_king_moves,
            ("black", "queens"): get_black_queen_moves,
            ("black", "rooks"): get_black_rook_moves,
            ("black", "bishops"): get_black_bishop_moves,
            ("black", "knights"): get_black_knight_moves,
            ("black", "pawns"): get_black_pawn_moves,
        }
        # TODO - Add support for en passant move detection
        return move_gens[(side, piece)](self, position)

    def search_forward(
        self, depth: int = 5, followed_path: list = None
    ) -> tuple[int, list]:
        """
        Recursively searches for all possible moves the board can make from this starting
        condition depth-first. Returns the best score achieved and the optimal path to take
        """
        if followed_path is None:
            followed_path = []
        if depth == 0:
            return self.score, followed_path

        optimal_score = 0
        optimal_path = []
        board_copy = self.copy()
        for side, piece in board_copy.board_pieces:
            positions = get_bit_positions(board_copy.get_bitboard(side, piece))
            for position in positions:
                moves = board_copy.get_moves(side, piece, position)
                for move in moves:
                    board_copy.move(start=position, end=move)
                    for opp_side, opp_piece in board_copy.opponent_pieces:
                        opp_positions = get_bit_positions(
                            board_copy.get_bitboard(opp_side, opp_piece)
                        )
                        for opp_pos in opp_positions:
                            opp_moves = board_copy.get_moves(
                                opp_side, opp_piece, opp_pos
                            )
                            for opp_move in opp_moves:
                                board_copy.move(opp_pos, opp_move)
                                next_score, next_path = board_copy.search_forward(
                                    depth - 1, followed_path + [(position, move)]
                                )
                                if next_score >= optimal_score:
                                    optimal_score = next_score
                                    optimal_path = next_path
                                board_copy.undo_move()
                    board_copy.undo_move()
                board_copy = self.copy()
        return optimal_score, optimal_path
