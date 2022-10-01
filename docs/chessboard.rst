.. _board_representation:

Internal Board Representation
===================================

**chessengine** uses bitboards to represent a chess board internally. A bitboard
is just a 64-bit integer in which each bit corresponds to one square on the chess
board (since a chess board also has 64 squares). A 1 at a certain position means
that a piece is present on that square, and a 0 means that no piece is present
on that square.

The board is defined in the :ref:`chessengine.bitboard.Board <Board>` class. It
stores the bitboards of all pieces for each side as attributes with the naming

convention ``<side>_<piece>s``. For example, you can access the bitboard
corresponding to black bishops by accessing the ``black_bishops`` attribute
on your ``Board`` object.

Available Attributes
--------------------

1. Attributes for White side

* white_bishops - A bitboard representing the positions of all white bishops on the board

* white_kings - A bitboard representing the position of the white king on the board

* white_knights - A bitboard representing the positions of all white knights on the board

* white_pawns - A bitboard representing the positions of all white pawns on the board

* white_queens - A bitboard representing the positions of all white queens on the board

* white_rooks - A bitboard representing the positions of all white rooks on the board

2. Attributes for Black side

* black_bishops - A bitboard representing the positions of all black bishops on the board

* black_kings - A bitboard representing the position of the black king on the board

* black_knights - A bitboard representing the positions of all black knights on the board

* black_pawns - A bitboard representing the positions of all black pawns on the board

* black_queens - A bitboard representing the positions of all black queens on the board

* black_rooks - A bitboard representing the positions of all black rooks on the board

3. Attributes for all pieces of White and Black side

* all_black - A bitboard representing the positions of all black pieces on the board

* all_white - A bitboard representing the positions of all white pieces on the board


4. Attributes for all pieces

* all_pieces - A bitboard representing the positions of all pieces on the board

5. Attributes for Chess Board

* board - A dictionary mapping tuples of the format (side, piece) to the corresponding bitboard. For example, board[("white", "pawns")] returns the bitboard corresponding to white pawns.

* moves - A list of all moves made on the board. Moves are stored as a tuple in the format (start, end, captured_side, captured_piece, captured_bitboard) where start is the position the piece started from, end is the position the piece landed on, captured_side is the side of the piece captured (if any, else None), captured_piece is the piece captured (if any, else None), and captured_bitboard is the bitboard of the captured piece before it was captured (used to restore it in case we want to undo moves).

* opponent_side - The side of the opponent. Can be "black" or "white"

* piece_count - A dictionary mapping tuples of the format (side, piece) to the number of pieces of that side on the board currently. For example, at the start of the game piece_count[("white", "pawns")] will be 8.

* side - The side of the board. Can be "black" or "white".
