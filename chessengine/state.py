class BoardState:
    """
    A class representing a chess board state
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
    
    def serialize(self):
        pass
    
    def set_state(self):
        pass
    
    # Define getters and setters for all bitboards in BoardState.board
    # so we can access as a class property instead of a dictionary lookup
    @property
    def white_pawns(self):
        return self.board[('white', 'pawns')]
    
    @white_pawns.setter
    def white_pawns(self, value):
        self.board[('white', 'pawns')] = value
    
    @property
    def white_rooks(self):
        return self.board[('white', 'rooks')]
    
    @white_rooks.setter
    def white_rooks(self, value):
        self.board[('white', 'rooks')] = value
        
    @property
    def white_knights(self):
        return self.board[('white', 'knights')]
    
    @white_knights.setter
    def white_knights(self, value):
        self.board[('white', 'knights')] = value
        
    @property
    def white_bishops(self):
        return self.board[('white', 'bishops')]
    
    @white_bishops.setter
    def white_bishops(self, value):
        self.board[('white', 'bishops')] = value
    
    @property
    def white_queens(self):
        return self.board[('white', 'queens')]
    
    @white_queens.setter
    def white_queens(self, value):
        self.board[('white', 'queens')] = value
        
    @property
    def white_kings(self):
        return self.board[('white', 'kings')]
    
    @white_kings.setter
    def white_kings(self, value):
        self.board[('white', 'kings')] = value

    @property
    def black_pawns(self):
        return self.board[('black', 'pawns')]

    @black_pawns.setter
    def black_pawns(self, value):
        self.board[('black', 'pawns')] = value

    @property
    def black_rooks(self):
        return self.board[('black', 'rooks')]

    @black_rooks.setter
    def black_rooks(self, value):
        self.board[('black', 'rooks')] = value

    @property
    def black_knights(self):
        return self.board[('black', 'knights')]

    @black_knights.setter
    def black_knights(self, value):
        self.board[('black', 'knights')] = value

    @property
    def black_bishops(self):
        return self.board[('black', 'bishops')]

    @black_bishops.setter
    def black_bishops(self, value):
        self.board[('black', 'bishops')] = value

    @property
    def black_queens(self):
        return self.board[('black', 'queens')]

    @black_queens.setter
    def black_queens(self, value):
        self.board[('black', 'queens')] = value

    @property
    def black_kings(self):
        return self.board[('black', 'kings')]

    @black_kings.setter
    def black_kings(self, value):
        self.board[('black', 'kings')] = value