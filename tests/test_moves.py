import unittest
from src.bitboard import Board
from src.moves import get_white_pawn_moves, get_white_rook_moves


class TestMoves(unittest.TestCase):
    def test_get_white_pawn_moves(self):
        board = Board("white")
        moves = get_white_pawn_moves(board, 2**8, False)
        self.assertEqual(moves, [2**16, 2**24])

        board.move(2**9, 2**16)
        self.assertEqual(get_white_pawn_moves(board, 2**8, False), [])
        
    def test_get_white_rook_moves(self):
        board = Board('white')
        moves = get_white_rook_moves(board, 1)
        self.assertEqual(moves, [])


if __name__ == "__main__":
    unittest.main()
