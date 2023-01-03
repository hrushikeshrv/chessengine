"""
A complete representation of the state of the chessboard
"""

import copy


class BoardState:
    """
    A class representing a chess board state. This class contains
    the following instance attributes -
    
    :ivar piece_count: A dictionary mapping pieces to the number of
        such pieces on the board. The keys are 2-tuples of the format
        ``(<side>, <piece>s)``. For example, ``piece_count[('white', 'kings')]``
        is 1.
    :ivar en_passant_position: The position on the board which a pawn
        can take by en passant.
    :ivar white_king_side_castle: A boolean indicating if white can castle
        king side.
    :ivar white_queen_side_castle: A boolean indicating if white can
        castle queen side.
    :ivar black_king_side_castle: A boolean indicating if black can castle
        king side.
    :ivar black_queen_side_castle: A boolean indicating if black can castle
        queen side.
    :ivar board: A dictionary mapping a piece type to its corresponding
        bitboard. The keys are 2-tuples of the format
        ``(<side>, <piece>s)``. For example, ``board[('white', 'rooks')]``
        returns the bitboard for white rooks.
    :ivar all_white: A bitboard containing the positions of all white pieces.
    :ivar all_black: A bitboard containing the positions of all black pieces.
    :ivar all_pieces: A bitboard containing the positions of all pieces on the board.
    
    Moreover, all the bitboards are accessible as class properties in the format
    ``<side>_<piece>s``. For example, the bitboard for black bishops can be
    accessed as the ``black_bishops`` property, and the bitboard for the black king
    can be accessed as the ``black_kings`` property. It is recommended to assign
    values to these properties instead of modifying the ``board`` dictionary
    directly, as this calls a setter method that also updates the board state's
    ``all_black``, ``all_white``, and ``all_pieces`` bitboards.
    """
    piece_count = {
        ("white", "kings"): 1,
        ("white", "queens"): 1,
        ("white", "rooks"): 2,
        ("white", "bishops"): 2,
        ("white", "knights"): 2,
        ("white", "pawns"): 8,
        ("black", "kings"): 1,
        ("black", "queens"): 1,
        ("black", "rooks"): 2,
        ("black", "bishops"): 2,
        ("black", "knights"): 2,
        ("black", "pawns"): 8,
    }
    
    en_passant_position = 0
    white_king_side_castle = True
    white_queen_side_castle = True
    black_king_side_castle = True
    black_queen_side_castle = True
    
    board = {
        ("white", "kings"): 16,
        ("white", "queens"): 8,
        ("white", "rooks"): 129,
        ("white", "bishops"): 36,
        ("white", "knights"): 66,
        ("white", "pawns"): 65280,
        ("black", "kings"): 1152921504606846976,
        ("black", "queens"): 576460752303423488,
        ("black", "rooks"): 9295429630892703744,
        ("black", "bishops"): 2594073385365405696,
        ("black", "knights"): 4755801206503243776,
        ("black", "pawns"): 71776119061217280,
    }
    
    all_white = (
            board[('white', 'kings')]
            | board[('white', 'queens')]
            | board[('white', 'rooks')]
            | board[('white', 'bishops')]
            | board[('white', 'knights')]
            | board[('white', 'pawns')]
    )
    all_black = (
            board[('black', 'kings')]
            | board[('black', 'queens')]
            | board[('black', 'rooks')]
            | board[('black', 'bishops')]
            | board[('black', 'knights')]
            | board[('black', 'pawns')]
    )
    all_pieces = all_white | all_black
    
    def serialize(self) -> dict:
        """
        Serializes the board state into a dictionary containing all the state
        attributes.
        
        :return: A dictionary with all the documented instance variables as keys
            and their respective values as values.
        """
        return {
            'piece_count': copy.copy(self.piece_count),
            'en_passant_position': self.en_passant_position,
            'white_king_side_castle': self.white_king_side_castle,
            'white_queen_side_castle': self.white_queen_side_castle,
            'black_king_side_castle': self.black_king_side_castle,
            'black_queen_side_castle': self.black_queen_side_castle,
            'board': copy.copy(self.board),
            'all_white': self.all_white,
            'all_black': self.all_black,
            'all_pieces': self.all_pieces,
        }

    def set_state(self, state: dict) -> None:
        """
        Given a dictionary of attributes, set the value of instance variables
        to be corresponding values.
        
        :param state: A dictionary containing the attributes to set
        """
        for key in state:
            setattr(self, key, state[key])
    
    def update_all_white(self) -> None:
        """
        Update the ``all_white`` bitboard if any white bitboard was changed
        """
        self.all_white = (
            self.board[('white', 'kings')]
            | self.board[('white', 'queens')]
            | self.board[('white', 'rooks')]
            | self.board[('white', 'bishops')]
            | self.board[('white', 'knights')]
            | self.board[('white', 'pawns')]
        )
        
    def update_all_black(self) -> None:
        """
        Update the ``all_black`` bitboard if any black bitboard was changed
        """
        self.all_black = (
            self.board[('black', 'kings')]
            | self.board[('black', 'queens')]
            | self.board[('black', 'rooks')]
            | self.board[('black', 'bishops')]
            | self.board[('black', 'knights')]
            | self.board[('black', 'pawns')]
        )
    
    def update_all_pieces(self) -> None:
        """
        Update the ``all_pieces`` bitboard if any bitboard was changed
        """
        self.all_pieces = self.all_white | self.all_black
    
    # Define getters and setters for all bitboards in BoardState.board,
    # so we can access as a class property instead of a dictionary lookup
    # and also update dependent bitboards.
    @property
    def white_pawns(self):
        """
        A bitboard representing the positions of all white pawns on the board.
        When this property is assigned to, it automatically updates the ``all_white``
        and ``all_pieces`` bitboard.
        """
        return self.board[('white', 'pawns')]
    
    @white_pawns.setter
    def white_pawns(self, value):
        self.board[('white', 'pawns')] = value
        self.update_all_white()
        self.update_all_pieces()
    
    @property
    def white_rooks(self):
        """
            A bitboard representing the positions of all white rooks on the board.
            When this property is assigned to, it automatically updates the ``all_white``
            and ``all_pieces`` bitboard.
        """
        return self.board[('white', 'rooks')]
    
    @white_rooks.setter
    def white_rooks(self, value):
        self.board[('white', 'rooks')] = value
        self.update_all_white()
        self.update_all_pieces()
        
    @property
    def white_knights(self):
        """
            A bitboard representing the positions of all white knights on the board.
            When this property is assigned to, it automatically updates the ``all_white``
            and ``all_pieces`` bitboard.
        """
        return self.board[('white', 'knights')]
    
    @white_knights.setter
    def white_knights(self, value):
        self.board[('white', 'knights')] = value
        self.update_all_white()
        self.update_all_pieces()
        
    @property
    def white_bishops(self):
        """
            A bitboard representing the positions of all white bishops on the board.
            When this property is assigned to, it automatically updates the ``all_white``
            and ``all_pieces`` bitboard.
        """
        return self.board[('white', 'bishops')]
    
    @white_bishops.setter
    def white_bishops(self, value):
        self.board[('white', 'bishops')] = value
        self.update_all_white()
        self.update_all_pieces()
    
    @property
    def white_queens(self):
        """
            A bitboard representing the positions of all white queens on the board.
            When this property is assigned to, it automatically updates the ``all_white``
            and ``all_pieces`` bitboard.
        """
        return self.board[('white', 'queens')]
    
    @white_queens.setter
    def white_queens(self, value):
        self.board[('white', 'queens')] = value
        self.update_all_white()
        self.update_all_pieces()
        
    @property
    def white_kings(self):
        """
            A bitboard representing the positions of the white king on the board.
            When this property is assigned to, it automatically updates the ``all_white``
            and ``all_pieces`` bitboard.
            """
        return self.board[('white', 'kings')]
    
    @white_kings.setter
    def white_kings(self, value):
        self.board[('white', 'kings')] = value
        self.update_all_white()
        self.update_all_pieces()

    @property
    def black_pawns(self):
        """
            A bitboard representing the positions of all black pawns on the board.
            When this property is assigned to, it automatically updates the ``all_black``
            and ``all_pieces`` bitboard.
        """
        return self.board[('black', 'pawns')]

    @black_pawns.setter
    def black_pawns(self, value):
        self.board[('black', 'pawns')] = value
        self.update_all_black()
        self.update_all_pieces()

    @property
    def black_rooks(self):
        """
            A bitboard representing the positions of all black rooks on the board.
            When this property is assigned to, it automatically updates the ``all_black``
            and ``all_pieces`` bitboard.
        """
        return self.board[('black', 'rooks')]

    @black_rooks.setter
    def black_rooks(self, value):
        self.board[('black', 'rooks')] = value
        self.update_all_black()
        self.update_all_pieces()

    @property
    def black_knights(self):
        """
            A bitboard representing the positions of all black knights on the board.
            When this property is assigned to, it automatically updates the ``all_black``
            and ``all_pieces`` bitboard.
        """
        return self.board[('black', 'knights')]

    @black_knights.setter
    def black_knights(self, value):
        self.board[('black', 'knights')] = value
        self.update_all_black()
        self.update_all_pieces()

    @property
    def black_bishops(self):
        """
            A bitboard representing the positions of all black bishops on the board.
            When this property is assigned to, it automatically updates the ``all_black``
            and ``all_pieces`` bitboard.
        """
        return self.board[('black', 'bishops')]

    @black_bishops.setter
    def black_bishops(self, value):
        self.board[('black', 'bishops')] = value
        self.update_all_black()
        self.update_all_pieces()

    @property
    def black_queens(self):
        """
            A bitboard representing the positions of all black queens on the board.
            When this property is assigned to, it automatically updates the ``all_black``
            and ``all_pieces`` bitboard.
        """
        return self.board[('black', 'queens')]

    @black_queens.setter
    def black_queens(self, value):
        self.board[('black', 'queens')] = value
        self.update_all_black()
        self.update_all_pieces()

    @property
    def black_kings(self):
        """
            A bitboard representing the positions of the black king on the board.
            When this property is assigned to, it automatically updates the ``all_black``
            and ``all_pieces`` bitboard.
        """
        return self.board[('black', 'kings')]

    @black_kings.setter
    def black_kings(self, value):
        self.board[('black', 'kings')] = value
        self.update_all_black()
        self.update_all_pieces()