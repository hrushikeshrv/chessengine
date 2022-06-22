import unittest
from src.bitboard import Board


class TestBoard(unittest.TestCase):
    def test_get_piece_bitboard(self):
        board = Board("white")
        self.assertEqual(board.get_piece_bitboard("black", "kings"), board.black_kings)
        self.assertEqual(board.get_piece_bitboard("white", "kings"), board.white_kings)
        self.assertEqual(board.get_piece_bitboard("white", "rooks"), board.white_rooks)
        self.assertEqual(board.get_piece_bitboard("black", "rooks"), board.black_rooks)

    def test_get_self_piece_bitboard(self):
        board = Board("white")
        self.assertEqual(board.get_self_piece_bitboard("pawns"), board.white_pawns)

    def test_set_piece_bitboard(self):
        board = Board("white")
        board.set_piece_bitboard("white", "pawns", 0)
        self.assertEqual(board.white_pawns, 0)

    def test_identify_piece_at(self):
        board = Board("white")
        self.assertEqual(
            board.identify_piece_at(2 ** 8), ("white", "pawns", board.white_pawns)
        )
        self.assertEqual(
            board.identify_piece_at(2 ** 7), ("white", "rooks", board.white_rooks)
        )

    def test_move(self):
        board = Board("white")
        board.move(2 ** 8, 2 ** 16)
        self.assertEqual(board.white_pawns, 0b11111111 << 9)
        board.move(2 ** 9, 2 ** 17)
        self.assertEqual(board.white_pawns, 0b11111111 << 10)

    def test_invalid_move(self):
        board = Board("white")
        with self.assertRaises(ValueError):
            board.move(1, 2 ** 8)


if __name__ == "__main__":
    unittest.main()
