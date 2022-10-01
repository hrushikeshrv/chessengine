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