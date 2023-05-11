"""
A complete bitboard representation of a chessboard, with all the methods needed
to play a game of chess.
"""


try:
    import importlib.resources as pkg_resources
except ImportError:
    # Python < 3.7
    pkg_resources = None
import random
import sys
from copy import copy
from math import log2
from time import sleep
from typing import Tuple, Iterable

from chessengine.exceptions import (
    PositionError,
    MoveError,
    PGNParsingError,
    GameNodeError,
)
from chessengine.moves import (
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
from chessengine.lookup_tables import (
    mask_position,
    clear_position,
    coords_to_pos,
    pos_to_coords,
    san_piece_map,
    piece_square_table,
)
from chessengine.utils import (
    get_bit_positions,
    get_file,
    get_rank,
    clear_lines,
    get_input,
    change_turn,
)
from chessengine.pgn.parser import PGNParser, SAN_MOVE_REGEX
from chessengine.pgn.utils import best_move_from_tree


class Board:
    """
    A class implementing a bitboard representation of a chess board.
    A particular bitboard can be accessed via the get_bitboard method or
    as an attribute with the name <side>_<piece>s. For example, ``white_pawns``,
    ``black_bishops``, ``white_queens``, ``black_kings``.

    :param side: The side that the _board_ will play. Should be one of "white" or "black"
    :var score: The score/evaluation of the current board positions. A higher/more positive score favors
        white, a lower/more negative score favors black
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

        self.score = 0

        if side.lower().strip() not in ["black", "white"]:
            raise ValueError(f'side must be one of "black" or "white". Got {side}')
        self.side = side.lower().strip()
        self.opponent_side = "black" if self.side == "white" else "white"
        self.en_passant_position = 0
        self.white_king_side_castle = True
        self.white_queen_side_castle = True
        self.black_king_side_castle = True
        self.black_queen_side_castle = True

        # Keep track of all moves made
        self.moves = []

    @property
    def board(self):
        """
        A dictionary mapping a side and piece to its corresponding bitboard.
        Useful when we want to iterate over all the bitboards of the board
        """
        return {
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

    @property
    def all_white(self):
        return (
            self.white_pawns
            | self.white_rooks
            | self.white_knights
            | self.white_bishops
            | self.white_queens
            | self.white_kings
        )

    @property
    def all_black(self):
        return (
            self.black_pawns
            | self.black_rooks
            | self.black_knights
            | self.black_bishops
            | self.black_queens
            | self.black_kings
        )

    @property
    def all_pieces(self):
        return (
            self.black_pawns
            | self.black_rooks
            | self.black_knights
            | self.black_bishops
            | self.black_queens
            | self.black_kings
            | self.white_pawns
            | self.white_rooks
            | self.white_knights
            | self.white_bishops
            | self.white_queens
            | self.white_kings
        )

    def __repr__(self):
        piece_list = ["." for _ in range(64)]
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
        ranks = ["8", "7", "6", "5", "4", "3", "2", "1"]
        files = [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]

        def add_bitboard_to_repr(board, s, p):
            board_string = bin(board)[2:]
            board_string = "0" * (64 - len(board_string)) + board_string
            for _ in range(64):
                if board_string[_] == "1":
                    piece_list[_] = unicode_piece[(s, p)]

        for side, piece in self.board:
            add_bitboard_to_repr(self.board[(side, piece)], side, piece)

        r = range(8)
        if self.side == "white":
            r = reversed(r)
            files = list(reversed(files))

        board_repr = ""
        board_repr += " " + " ".join(files) + "\n"

        for i in r:
            board_repr += ranks[i] + "  "

            if self.side == "white":
                board_repr += " ".join(piece_list[8 * i : 8 * i + 8])
            else:
                board_repr += " ".join(piece_list[8 * i : 8 * i + 8][::-1])

            board_repr += "  " + ranks[i]
            board_repr += "\n"

        board_repr += " " + " ".join(files) + "\n"
        return board_repr

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if self.side != other.side:
            return False
        return str(self) == str(other)

    def __hash__(self):
        hash_str = f"{self.side[0]} "
        for side, piece in [
            ("white", "kings"),
            ("white", "queens"),
            ("white", "rooks"),
            ("white", "bishops"),
            ("white", "knights"),
            ("white", "pawns"),
            ("black", "kings"),
            ("black", "queens"),
            ("black", "rooks"),
            ("black", "bishops"),
            ("black", "knights"),
            ("black", "pawns"),
        ]:
            hash_str += str(self.board[(side, piece)]) + " "
        return hash(hash_str)

    @property
    def board_pieces(self):
        """
        A list of all bitboards of the pieces that belong to the Board.
        """
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
        """
        A list of all bitboards of the pieces that belong to the opponent.
        """
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
        """
        Create and return a copy of the board.
        """
        return copy(self)

    def evaluate_score(self) -> int:
        """
        Evaluate the current score/evaluation of the board state. Use this method to
        reset the board score to the correct value if the game starts from an intermediate
        stage.

        :return: The score/evaluation of the current board state.
        """
        s = 0
        piece_values = {
            "pawns": 100,
            "rooks": 500,
            "knights": 320,
            "bishops": 330,
            "queens": 900,
            "kings": 20000,
        }
        for i in range(64):
            pos = 2**i
            side, piece, _ = self.identify_piece_at(pos)
            if side is None:
                continue
            elif side == "white":
                s += piece_values[piece] + piece_square_table[(side, piece)][i]
            else:
                s -= piece_values[piece] + piece_square_table[(side, piece)][i]

        return s

    def get_side_bitboard(self, side: str) -> int:
        """
        Returns the bitboard containing all pieces for the given side.

        :param side: "white" or "black"
        :return: If ``side == "white"``, returns ``self.all_white``, else ``self.all_black``
        """
        if side == "white":
            return self.all_white
        return self.all_black

    def get_bitboard(self, side: str, piece: str) -> int:
        """
        Returns the bitboard of the passed side for the passed pieces.
        For example, calling with side="black" and piece="king" will return the black_kings bitboard, and so on.

        Raises AttributeError if a bitboard with an invalid name is requested. See above for the bitboard naming
        convention.

        :param side: "white" or "black"
        :param piece: Can be one of - "kings", "queens", "bishops", "knights", "rooks", "pawns"
        :return: Bitboard
        """
        attrname = side + "_" + piece
        return getattr(self, attrname)

    def get_self_piece_bitboard(self, piece: str) -> int:
        """
        Returns the bitboard corresponding to the passed piece, considering the board's
        own side. i.e. - If the board is white, calling with piece="king" will return
        white king, etc.

        :param piece: Can be one of - "kings", "queens", "bishops", "knights", "rooks", "pawns"
        :return: Bitboard
        """
        return self.get_bitboard(side=self.side, piece=piece)

    def set_bitboard(self, side: str, piece: str, board: int) -> None:
        """
        Sets the bitboard for the passed arguments to the passed bitboard

        :param side: "white" or "black"
        :param piece: Can be one of - "kings", "queens", "bishops", "knights", "rooks", "pawns"
        :param board: The bitboard to be set
        """
        attrname = side + "_" + piece
        setattr(self, attrname, board)

    def identify_piece_at(self, position: int) -> tuple:
        """
        Identifies if there is any piece on the position passed.

        :param position: A power of 2 corresponding to a position on the board. See :ref:`position_representation`
        :return: Returns a 3-tuple of the format (side, piece, bitboard) where side is the side of
            the piece identified at position (e.g, "black"), piece is the type of piece identified
            at position (e.g, "bishops"), and bitboard is the bitboard of the piece (e.g, Board.black_bishops).
        """
        if not position & self.all_pieces:
            return None, None, None
        for side, piece in self.board:
            board = self.board[(side, piece)]
            if board & position > 0:
                return side, piece, board

    def move(self, start: int, end: int, score: int = None, track: bool = True) -> None:
        """
        Moves the piece at start to end. Doesn't check anything, just makes
        the move (unless the start or end positions are invalid). Also checks if move
        is a castle, moves the rook automatically on castle, and updates each
        side's ability to castle on each move.

        .. important::
            This is the underlying function that is called by both ``Board.move_san`` and
            ``Board.move_raw``. This function keeps track of castling status, but performs
            no validation. ``Board.move_san`` and ``Board.move_raw`` perform validation,
            but don't keep track of castling status. In general, you should use ``Board.move_san``
            or ``Board.move_raw`` inside the game loop to ensure both move validation and
            castling status are correctly performed/updated. Only use ``Board.move`` in special
            cases when you want to make arbitrary moves outside the rules and/or the game loop.

        :param start: The start position of the move. See :ref:`position_representation`
        :param end: The end position of the move. See :ref:`position_representation`
        :param score: The new score/evaluation of the board after the move is made
        :param track: If ``True``, the move made will be stored in self.moves

        :raises PositionError: If an invalid position was passed.
        """
        if not 1 <= start <= 2**63:
            raise PositionError(
                f"The start position is outside the board - moving from {log2(start)} to {log2(end)}"
            )
        if not 1 <= end <= 2**63:
            raise PositionError(
                f"The end position is outside the board - moving from {log2(start)} to {log2(end)}"
            )

        start_side, start_piece, start_board = self.identify_piece_at(start)
        if start_side is None:
            raise PositionError(f"There is no piece at position {log2(start)} to move")

        end_side, end_piece, end_board = self.identify_piece_at(end)
        if end_side == start_side:
            raise PositionError(
                f"Can't move from {log2(start)} to {log2(end)}, both positions have {end_side} pieces."
            )

        # Identify if the move is a castle and what type of castle it is
        castle_type = None
        # Don't set castling flags if we're not tracking this move
        if track:
            if start_piece == "kings":
                if start_side == "white":
                    self.white_king_side_castle = False
                    self.white_queen_side_castle = False
                    if start == 2**4:
                        if end == 2**6:
                            castle_type = "white_kingside"
                        if end == 2**2:
                            castle_type = "white_queenside"
                if start_side == "black":
                    self.black_king_side_castle = False
                    self.black_queen_side_castle = False
                    if start == 2**60:
                        if end == 2**62:
                            castle_type = "black_kingside"
                        if end == 2**58:
                            castle_type = "black_queenside"

            # Set castling ability to false when rook is moved
            if start_piece == "rooks":
                if start_side == "white" and start == 1:
                    self.white_queen_side_castle = False
                elif start_side == "white" and start == 2**7:
                    self.white_king_side_castle = False
                elif start_side == "black" and start == 2**63:
                    self.black_king_side_castle = False
                elif start_side == "black" and start == 2**56:
                    self.black_queen_side_castle = False

        # Track moves made so we can undo
        if track:
            start_state = (
                start,
                end,
                end_side,
                end_piece,
                end_board,
                castle_type,
                self.score,
                self.white_king_side_castle,
                self.white_queen_side_castle,
                self.black_king_side_castle,
                self.black_queen_side_castle,
            )
            self.moves.append(start_state)

        # Check en passant moves
        if start_piece == "pawns":
            if start_side == "white":
                # Check en passant status
                if get_rank(start) == 2 and get_rank(end) == 4:
                    self.en_passant_position = start << 8

                # Check if a pawn captured by an en passant move
                elif end == self.en_passant_position:
                    # White pawn made an en passant move
                    black_pawn_bb = self.get_bitboard("black", "pawns")
                    black_pawn_bb &= clear_position[end >> 8]
                    self.set_bitboard("black", "pawns", black_pawn_bb)
                    self.en_passant_position = 0

                # Clear self.en_passant_position
                else:
                    self.en_passant_position = 0

            else:
                # Check en passant status
                if get_rank(start) == 7 and get_rank(end) == 5:
                    self.en_passant_position = start >> 8

                # Check if a pawn captured by an en passant move
                elif end == self.en_passant_position:
                    # Black pawn made an en passant move
                    white_pawn_bb = self.get_bitboard("white", "pawns")
                    white_pawn_bb &= clear_position[end << 8]
                    self.set_bitboard("white", "pawns", white_pawn_bb)
                    self.en_passant_position = 0

                # Clear self.en_passant_position
                else:
                    self.en_passant_position = 0

        else:
            self.en_passant_position = 0

        if end_piece is not None:
            # Clear the captured piece's position (set "end" to 0)
            opp_side_board = self.get_bitboard(end_side, end_piece)
            opp_side_board &= clear_position[end]
            self.set_bitboard(end_side, end_piece, opp_side_board)

        # Clear the moved piece's original position (set "start" to 0)
        move_side_board = self.get_bitboard(start_side, start_piece)
        move_side_board &= clear_position[start]

        # Set the moved piece's final position (set "end" to 1)
        move_side_board |= mask_position[end]
        self.set_bitboard(start_side, start_piece, move_side_board)

        # If the move was a castle, also move the rook into the correct position
        # Validity of castling is not checked
        if castle_type == "white_kingside":
            self.move(2**7, 2**5, False)  # Don't track this move
            self.white_king_side_castle = False
            self.white_queen_side_castle = False
        elif castle_type == "white_queenside":
            self.move(2**0, 2**3, False)  # Don't track this move
            self.white_king_side_castle = False
            self.white_queen_side_castle = False
        elif castle_type == "black_kingside":
            self.move(2**63, 2**61, False)  # Don't track this move
            self.black_king_side_castle = False
            self.black_queen_side_castle = False
        elif castle_type == "black_queenside":
            self.move(2**56, 2**59, False)  # Don't track this move
            self.black_king_side_castle = False
            self.black_queen_side_castle = False

        # Update the board evaluation
        if track:
            if score is None:
                score = self.evaluate_score()
            self.score = score

    def move_raw(self, start: int, end: int, track: bool = True) -> None:
        """
        Moves the piece at start to end. Checks if the move is a valid move
        to make given the current state of the board.

        :param start: The start position of the move. See :ref:`position_representation`
        :param end: The end position of the move. See :ref:`position_representation`
        :param track: If ``True``, the move made will be stored in self.moves

        :raises PositionError: If there is not piece at ``start`` to move
        :raises MoveError: If an invalid move is passed
        """
        side, piece, board = self.identify_piece_at(start)
        if side is None:
            raise PositionError(
                f"There is no piece at {pos_to_coords[int(log2(start))]} to move."
            )
        moves = self.get_moves(side=side, piece=piece)
        if (start, end) not in moves:
            raise MoveError(
                f"{pos_to_coords[int(log2(start))]} to {pos_to_coords[int(log2(end))]} is not a valid move for {side}"
            )
        self.move(start=start, end=end, track=track)

    def move_san(self, move: str, side: str) -> None:
        """
        Make a move given in standard algebraic notation.

        :param move: A move given in SAN
        :param side: "white" or "black"

        :raises MoveError: If an ambiguous or invalid move was passed
        :raises PGNParsingError: If the move was invalid SAN
        """
        if "0-0-0" in move or "O-O-O" in move:
            # queen side castle
            if side == "white":
                if self.white_queen_side_castle:
                    self.move(2**4, 2**2)
                else:
                    raise MoveError(
                        f'White cannot castle, it has already moved the {"rook" if self.white_king_side_castle else "king"}.'
                    )
                self.white_queen_side_castle = False
                self.white_king_side_castle = False
            else:
                if self.black_queen_side_castle:
                    self.move(2**60, 2**58)
                else:
                    raise MoveError(
                        f'Black cannot castle, it has already moved the {"rook" if self.black_king_side_castle else "king"}.'
                    )
                self.black_queen_side_castle = False
                self.black_king_side_castle = False
        elif "0-0" in move or "O-O" in move:
            # king side castle
            if side == "white":
                if self.white_king_side_castle:
                    self.move(2**4, 2**6)
                else:
                    raise MoveError(
                        f'White cannot castle, it has already moved the {"rook" if self.white_queen_side_castle else "king"}.'
                    )
                self.white_king_side_castle = False
                self.white_queen_side_castle = False
            else:
                if self.black_king_side_castle:
                    self.move(2**60, 2**62)
                else:
                    raise MoveError(
                        f'Black cannot castle, it has already moved the {"rook" if self.black_queen_side_castle else "king"}.'
                    )
                self.black_king_side_castle = False
                self.black_queen_side_castle = False
        else:
            # regular move
            match = SAN_MOVE_REGEX.match(move)
            if match is None:
                raise PGNParsingError(f'Couldn\'t parse move "{move}".')

            groups = match.groups()
            if groups[0] is None:
                piece_moved = san_piece_map["P"]
            else:
                piece_moved = san_piece_map[groups[0].upper()]

            end_pos = 2 ** coords_to_pos[groups[2].upper()]
            moves = self.get_moves(side, piece_moved)

            if groups[1] is None:
                # No rank or file provided in the SAN
                candidate_move = None
                for m in moves:
                    if m[1] == end_pos:
                        if candidate_move:
                            raise MoveError(
                                f"{move} is ambiguous for {side}. Specify a file or rank to move from."
                            )
                        candidate_move = m
                if candidate_move is None:
                    raise MoveError(f"{move} is not a valid move for {side}.")
                self.move(
                    start=candidate_move[0],
                    end=candidate_move[1],
                    score=candidate_move[2],
                )
            elif groups[1].isalpha():
                # File provided in the SAN
                candidate_move = None
                for m in moves:
                    file = get_file(m[0])
                    if groups[1].upper() == "ABCDEFGH"[file - 1] and m[1] == end_pos:
                        if candidate_move:
                            raise MoveError(
                                f"{move} is ambiguous for {side}. Specify a rank to move from."
                            )
                        candidate_move = m
                if candidate_move is None:
                    raise MoveError(f"{move} is not valid for {side}.")
                self.move(
                    start=candidate_move[0],
                    end=candidate_move[1],
                    score=candidate_move[2],
                )
            elif groups[1].isnumeric():
                # Rank provided in the SAN
                candidate_move = None
                for m in moves:
                    rank = get_rank(m[0])
                    if groups[1] == "12345678"[rank - 1] and m[1] == end_pos:
                        if candidate_move:
                            raise MoveError(
                                f"{move} is ambiguous for {side}. Specify a file to move from."
                            )
                        candidate_move = m
                if candidate_move is None:
                    raise MoveError(f"{move} is not a valid move for {side}.")
                self.move(
                    start=candidate_move[0],
                    end=candidate_move[1],
                    score=candidate_move[2],
                )
            elif groups[1].isalnum():
                # Both rank and file provided in the SAN
                start_pos = 2 ** coords_to_pos[groups[1].upper()]
                for m in moves:
                    if m[0] == start_pos and m[1] == end_pos:
                        self.move(start=start_pos, end=end_pos, score=m[2])
                        break
                else:
                    raise MoveError(f"{move} is not a valid move for {side}.")

    def make_moves(self, *moves: Iterable[tuple[int, int]]) -> None:
        """
        Given a number of moves as tuples (start, end), call
        Board.move on all. Tracks all moves by default in ``self.moves``
        """
        for start, end in moves:
            self.move(start, end)

    def undo_move(self) -> None:
        """
        Undo the last tracked move.
        """
        if not self.moves:
            raise RuntimeError("No moves have been made yet to undo.")
        (
            end,
            start,
            side,
            piece,
            board,
            castle_type,
            prev_score,
            white_king_side_castle,
            white_queen_side_castle,
            black_king_side_castle,
            black_queen_side_castle,
        ) = self.moves.pop()
        self.score = prev_score
        self.white_king_side_castle = white_king_side_castle
        self.white_queen_side_castle = white_queen_side_castle
        self.black_king_side_castle = black_king_side_castle
        self.black_queen_side_castle = black_queen_side_castle

        if castle_type is not None:
            if castle_type == "white_kingside":
                self.move(start=start, end=end, track=False)  # Move king
                self.move(2**5, 2**7, track=False)  # Move rook
            elif castle_type == "white_queenside":
                self.move(start=start, end=end, track=False)  # Move king
                self.move(2**3, 2**0, track=False)  # Move rook
            elif castle_type == "black_kingside":
                self.move(start=start, end=end, track=False)  # Move king
                self.move(2**61, 2**63, track=False)  # Move rook
            elif castle_type == "black_queenside":
                self.move(start=start, end=end, track=False)  # Move king
                self.move(2**59, 2**56, track=False)  # Move rook
        else:
            self.move(start=start, end=end, track=False)
            if side is not None:
                self.set_bitboard(side, piece, board)

    def get_moves(
        self, side: str, piece: str = None, position: int = None
    ) -> list[tuple[int, int, int]]:
        """
        Get all end positions a piece of side can reach starting from position.
        ``side`` is always required, piece and position are optional.

        If piece is not specified, gets all moves for all pieces of the passed side, i.e. get
        all valid moves for white or black.

        If side and piece are specified and position is not, gets all valid moves for the
        specified side and piece on the board, i.e. if side is "white" and piece is "rooks",
        gets all valid moves for all white rooks on the board.

        If side, piece, and position are specified, gets all moves for the piece present on position.

        :param side: "white" or "black"
        :param piece: Can be one of - "kings", "queens", "bishops", "knights", "rooks", "pawns"
        :param position: A power of 2 corresponding to a position on the board. See :ref:`position_representation`
        :return: A list of moves as tuples ``(start, end)``, where ``start`` and ``end`` are positions on the board.
            See :ref:`position_representation`
        """
        if piece is not None:
            if position is None:
                moves = []
                positions = get_bit_positions(self.get_bitboard(side, piece))
                for position in positions:
                    moves.extend(self.get_moves(side, piece, position))
                return moves
            else:
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
                return move_gens[(side, piece)](self, position)
        else:
            moves = []
            if side == self.side:
                pieces = self.board_pieces
            else:
                pieces = self.opponent_pieces
            for side, piece in pieces:
                positions = get_bit_positions(self.get_bitboard(side, piece))
                for position in positions:
                    moves.extend(self.get_moves(side, piece, position))
            return moves

    def search_forward(self, depth: int = 4) -> tuple[int, tuple[int, int, int]]:
        """
        Execute an alpha-beta pruned depth-first search to find the optimal move from
        the current board state.

        :param depth: int - The number of plies to search (1 move is 2 plies). Default = 4 plies.
        :return: A 2-tuple where the first element is the best board score found, and the second
            element is the best found move as a 2 tuple containing the start position and the end position
        """
        maximize = self.side == "white"
        best_score = -100000 if maximize else 100000

        moves = self.get_moves(self.side)
        best_move = moves[0]

        for move in moves:
            self.move(start=move[0], end=move[1], score=move[2])
            value = self.alpha_beta_search(
                depth=depth - 1, maximizing_player=not maximize
            )
            self.undo_move()

            if maximize and value >= best_score:
                best_score = value
                best_move = move
            elif not maximize and value <= best_score:
                best_score = value
                best_move = move
        return best_score, best_move

    def alpha_beta_search(
        self,
        depth: int = 4,
        alpha: int = -100000,
        beta: int = 100000,
        maximizing_player: bool = True,
    ) -> int:
        """
        Execute an alpha-beta pruned search. You probably won't need to
        call this function yourself, use Board.search_forward instead.

        :param depth: The number of plies to search forward (default=4)
        :param alpha: The minimum score that the maximizing player is guaranteed (default=-1000). You probably won't need to specify this argument.
        :param beta: The maximum score that the minimizing player is guaranteed (default=1000). You probably won't need to specify this argument.
        :param maximizing_player: True if white is searching for a move, False if black is searching for a move.

        :return: The score of the best board position found.
        """
        if depth == 0:
            return self.score

        if maximizing_player:
            value = -100000
            moves = self.get_moves(self.side)
            for move in moves:
                self.move(start=move[0], end=move[1], score=move[2])
                final_score = self.alpha_beta_search(depth - 1, alpha, beta, False)
                value = max(value, final_score)
                self.undo_move()
                if value >= beta:
                    break
                alpha = max(alpha, value)
            return value
        else:
            value = 100000
            moves = self.get_moves(self.opponent_side)
            for move in moves:
                self.move(start=move[0], end=move[1], score=move[2])
                final_score = self.alpha_beta_search(depth - 1, alpha, beta, True)
                value = min(value, final_score)
                self.undo_move()
                if value <= alpha:
                    break
                beta = min(beta, value)
            return value

    def handle_player_move(
        self, side_to_move: str, last_move: str
    ) -> Tuple[str, int, bool]:
        """
        Ask for user input until accepted. When a valid input is received, execute the move.

        :param side_to_move: "white" or "black"
        :param last_move: The last move made by the board to print out to the user
        :return: A 3-tuple of the form - the valid (move, lines_printed, move_undone)
            where move is the valid move received as input, lines_printed is the number
            of lines printed, and move_undone is a boolean that is ``True`` when the user
            chose to undo their previous move
        """
        move = ""
        lines_added = 0
        input_accepted = False

        while not input_accepted:
            print(last_move)
            move = get_input(
                f"Enter your move in standard algebraic notation ({side_to_move.capitalize()}'s turn) - "
            )
            lines_added += 2
            if move.lower() == "q":
                print("Thanks for playing!")
                sys.exit(0)
            if move.lower() == "u":
                try:
                    self.undo_move()
                    self.undo_move()  # Undo both player's moves
                except RuntimeError:
                    print("No moves have been made yet to undo!")
                    lines_added += 1
                return move, lines_added, True
            # Input was normal move
            try:
                if " to " in move:
                    # Input was not in SAN
                    _ = move.upper().strip().split()
                    start = 2 ** coords_to_pos[_[0]]
                    end = 2 ** coords_to_pos[_[-1]]
                    self.move_raw(start=start, end=end)
                else:
                    # Input was in SAN
                    self.move_san(move=move, side=side_to_move)
                input_accepted = True
                last_move = f"{side_to_move.capitalize()} moved {move}"
            except (MoveError, PositionError, PGNParsingError) as e:
                print(e)
                lines_added += 1
            except KeyError as e:
                print(f"{e} is not a valid square. Please try again.")
                lines_added += 1
        return move, lines_added, False

    def play(self, search_depth: int = 4) -> None:
        """
        Play a game of chess against the computer.

        :param search_depth: The number of plies the computer should search forward. Be careful
            passing values about 4 as the search depth. It increases the running time of the
            move search exponentially.
        """
        parser = None
        if pkg_resources is not None:
            loading_messages = [
                "Searching for opening moves.",
                "Reading an opening book.",
                "Waking up.",
                "Building move tree.",
            ]

            parser = PGNParser()
            print(random.choice(loading_messages))
            opening_files = pkg_resources.contents("chessengine.openings")
            for child in opening_files:
                file_path = pkg_resources.path("chessengine.openings", child)
                with file_path as f:
                    if f.suffix == ".pgn":
                        print(".", end="", flush=True)
                        parser.parse(f)
            print(f"\nRead through {len(parser.games)} games.")
        sleep(1)
        print(f"Set search depth to {search_depth}")
        sleep(0.7)

        print(self)
        side_to_move = "white"
        in_game_tree = parser is not None
        current_node = parser.root_node if in_game_tree else None
        lines_printed = 11
        last_move = ""
        while True:
            clear_lines(lines_printed)
            print(self)
            lines_printed = 11
            if side_to_move == self.side:
                if in_game_tree:
                    move, node = random.choice(list(current_node.children.items()))
                    self.move_san(move=move, side=side_to_move)
                    current_node = node
                    last_move = f"Board moves {move}"
                else:
                    best_score, best_move = self.search_forward(search_depth)
                    self.move(best_move[0], best_move[1])
                    last_move = f"Board moves from {pos_to_coords[log2(best_move[0])]} to {pos_to_coords[log2(best_move[1])]}"
            else:
                move, lines_added, move_undone = self.handle_player_move(
                    side_to_move, last_move
                )
                lines_printed += lines_added
                last_move = f"{side_to_move.capitalize()} moved {move}"

                if move_undone:
                    # return to outer loop, so both sides need to make a new move
                    continue
                if in_game_tree:
                    try:
                        current_node = current_node.get_child(move)
                    except GameNodeError:
                        in_game_tree = False
                print(f"You moved {move}")
                lines_printed += 1

            side_to_move = change_turn(side_to_move)

    def play_pvp(self) -> None:
        """
        Play a game of chess on the terminal with another player
        """
        print(self)
        lines_printed = 11

        side_to_move = "white"
        last_move = ""
        while True:
            clear_lines(lines_printed)
            print(self)
            lines_printed = 11

            move, lines_added, move_undone = self.handle_player_move(
                side_to_move, last_move
            )
            lines_printed += lines_added
            last_move = f"{side_to_move.capitalize()} moved {move}"

            if (
                move_undone
            ):  # return to outer loop, so both sides need to make a new move
                continue

            side_to_move = change_turn(side_to_move)
