import unittest
from chessengine.bitboard import Board
from chessengine.moves import (
    get_white_pawn_moves,
    get_white_rook_moves,
    get_white_bishop_moves,
    get_white_knight_moves,
    get_white_king_moves,
)


# TODO - Add tests for black pieces
class TestMoves(unittest.TestCase):
    def test_get_white_pawn_moves(self):
        board = Board("white")
        moves = get_white_pawn_moves(board, 2**8, False)
        self.assertEqual(moves, [(2**8, 2**16), (2**8, 2**24)])

        board.move(2**9, 2**16)
        self.assertEqual(get_white_pawn_moves(board, 2**8, False), [])

        board.move(2**8, 2**49)
        self.assertEqual(
            get_white_pawn_moves(board, 2**49, False),
            [(2**49, 2**56), (2**49, 2**58)],
        )

    def test_get_white_rook_moves(self):
        board = Board("white")
        moves = get_white_rook_moves(board, 1)
        self.assertEqual(moves, [])

        board.move(2**8, 2**16)
        moves = get_white_rook_moves(board, 1)
        self.assertEqual(moves, [(1, 2**8)])

        board = Board("white")
        board.move(1, 2**28)
        moves = get_white_rook_moves(board, 2**28)
        self.assertEqual(
            moves,
            [
                (2**28, 2**36),
                (2**28, 2**44),
                (2**28, 2**52),
                (2**28, 2**20),
                (2**28, 2**29),
                (2**28, 2**30),
                (2**28, 2**31),
                (2**28, 2**27),
                (2**28, 2**26),
                (2**28, 2**25),
                (2**28, 2**24),
            ],
        )

    def test_get_white_bishop_moves(self):
        board = Board("white")
        moves = get_white_bishop_moves(board, 4)
        self.assertEqual(moves, [])

        board.move(4, 2**18)
        moves = get_white_bishop_moves(board, 2**18)
        self.assertEqual(
            moves,
            [
                (2**18, 2**27),
                (2**18, 2**36),
                (2**18, 2**45),
                (2**18, 2**54),
                (2**18, 2**25),
                (2**18, 2**32),
            ],
        )

    def test_get_white_knight_moves(self):
        board = Board("white")
        moves = get_white_knight_moves(board, 2)
        self.assertEqual(moves, [(2, 2**16), (2, 2**18)])

        board.move(2, 2**26)
        moves = get_white_knight_moves(board, 2**26)
        self.assertEqual(
            moves,
            [
                (2**26, 2**16),
                (2**26, 2**20),
                (2**26, 2**41),
                (2**26, 2**43),
                (2**26, 2**32),
                (2**26, 2**36),
            ],
        )

    def test_get_white_king_moves(self):
        board = Board("white")
        moves = get_white_king_moves(board, 16)
        self.assertEqual(moves, [])

        board.move(2**4, 2**28)
        moves = get_white_king_moves(board, 2**28)
        self.assertEqual(
            moves,
            [
                (2**28, 2**20),
                (2**28, 2**19),
                (2**28, 2**21),
                (2**28, 2**36),
                (2**28, 2**35),
                (2**28, 2**37),
                (2**28, 2**27),
                (2**28, 2**29),
            ],
        )

        board.move(2**11, 2**19)
        moves = get_white_king_moves(board, 2**28)
        self.assertEqual(
            moves,
            [
                (2**28, 2**20),
                (2**28, 2**21),
                (2**28, 2**36),
                (2**28, 2**35),
                (2**28, 2**37),
                (2**28, 2**27),
                (2**28, 2**29),
            ],
        )


if __name__ == "__main__":
    unittest.main()
