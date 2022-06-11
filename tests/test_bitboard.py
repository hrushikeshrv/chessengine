import unittest
from src.bitboard import Board


class TestBoard(unittest.TestCase):
    def test_get_piece_bitboard(self):
        board = Board('white')
        self.assertEqual(board.get_piece_bitboard('black', 'kings'), board.black_kings)
        self.assertEqual(board.get_piece_bitboard('white', 'kings'), board.white_kings)
        self.assertEqual(board.get_piece_bitboard('white', 'rooks'), board.white_rooks)
        self.assertEqual(board.get_piece_bitboard('black', 'rooks'), board.black_rooks)
    
    def test_get_self_piece_bitboard(self):
        board = Board('white')
        self.assertEqual(board.get_self_piece_bitboard('pawns'), board.white_pawns)
    
    def test_set_piece_bitboard(self):
        board = Board('white')
        board.set_piece_bitboard('white', 'pawns', 0)
        self.assertEqual(board.white_pawns, 0)
