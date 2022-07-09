import unittest
from src.bitboard import Board
from src.moves import (
    get_white_pawn_moves,
    get_white_rook_moves,
    get_white_bishop_moves,
    get_white_knight_moves,
)


class TestMoves(unittest.TestCase):
    def test_get_white_pawn_moves(self):
        board = Board("white")
        moves = get_white_pawn_moves(board, 2**8, False)
        self.assertEqual(moves, [2**16, 2**24])

        board.move(2**9, 2**16)
        self.assertEqual(get_white_pawn_moves(board, 2**8, False), [])

    def test_get_white_rook_moves(self):
        board = Board("white")
        moves = get_white_rook_moves(board, 1)
        self.assertEqual(moves, [])

        board.move(2**8, 2**16)
        moves = get_white_rook_moves(board, 1)
        self.assertEqual(moves, [2**8])

        board = Board("white")
        board.move(1, 2**28)
        moves = get_white_rook_moves(board, 2**28)
        self.assertEqual(
            moves,
            [
                2**36,
                2**44,
                2**52,
                2**20,
                2**29,
                2**30,
                2**31,
                2**27,
                2**26,
                2**25,
                2**24,
            ],
        )

    def test_get_white_bishop_moves(self):
        board = Board("white")
        moves = get_white_bishop_moves(board, 4)
        self.assertEqual(moves, [])

        board.move(4, 2**18)
        moves = get_white_bishop_moves(board, 2**18)
        self.assertEqual(moves, [2**27, 2**36, 2**45, 2**54, 2**25, 2**32])

    def test_get_white_knight_moves(self):
        board = Board("white")
        moves = get_white_knight_moves(board, 2)
        self.assertEqual(moves, [2**16, 2**18])

        board.move(2, 2**26)
        moves = get_white_knight_moves(board, 2**26)
        self.assertEqual(moves, [2**16, 2**20, 2**41, 2**43, 2**32, 2**36])


if __name__ == "__main__":
    unittest.main()
