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
        board = Board("white")
        moves = get_white_rook_moves(board, 1)
        self.assertEqual(moves, [])

        board.move(2**8, 2**16)
        moves = get_white_rook_moves(board, 1)
        self.assertEqual(moves, [2**8])
        
        board.move(2, 2**17)
        board.move(4, 2**18)
        board.move(8, 2**19)
        moves = get_white_rook_moves(board, 1)
        self.assertEqual(moves, [2**8, 2**1, 2**2, 2**3])
        
        board.move(1, 2**35)
        moves = set(get_white_rook_moves(board, 2**35))
        self.assertEqual(moves, {2 ** 19, 2 ** 27, 2**43, 2**32, 2**33, 2**34, 2**36, 2**37, 2**38, 2**39})


if __name__ == "__main__":
    unittest.main()
