import unittest
from unittest.mock import patch
from chessengine.bitboard import Board
from typing import Optional, List


class TestBoard(unittest.TestCase):
    def test_get_bitboard(self):
        board = Board("white")
        self.assertEqual(board.get_bitboard("black", "kings"), board.black_kings)
        self.assertEqual(board.get_bitboard("white", "kings"), board.white_kings)
        self.assertEqual(board.get_bitboard("white", "rooks"), board.white_rooks)
        self.assertEqual(board.get_bitboard("black", "rooks"), board.black_rooks)

    def test_get_self_piece_bitboard(self):
        board = Board("white")
        self.assertEqual(board.get_self_piece_bitboard("pawns"), board.white_pawns)

    def test_set_piece_bitboard(self):
        board = Board("white")
        board.set_bitboard("white", "pawns", 0)
        self.assertEqual(board.white_pawns, 0)

    def test_identify_piece_at(self):
        board = Board("white")
        self.assertEqual(
            board.identify_piece_at(2**8), ("white", "pawns", board.white_pawns)
        )
        self.assertEqual(
            board.identify_piece_at(2**7), ("white", "rooks", board.white_rooks)
        )
        self.assertEqual(board.identify_piece_at(2**20), (None, None, None))

    def test_move(self):
        board = Board("white")
        board.move(2**8, 2**16)
        self.assertEqual(board.white_pawns, 0b11111111 << 9)
        board.move(2**9, 2**17)
        self.assertEqual(board.white_pawns, 0b11111111 << 10)

    def test_invalid_move(self):
        board = Board("white")
        with self.assertRaises(ValueError):
            board.move(1, 2**8)

    def test_fen_representation(self):
        return  # Skip this test, FEN representation is deprecated
        board = Board("white")
        self.assertEqual(
            board.FEN,
            "rnbqkbnr/pppppppp/00000000/00000000/00000000/00000000/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        )

        board.move(2**8, 2**16)
        self.assertEqual(
            board.FEN,
            "rnbqkbnr/pppppppp/00000000/00000000/00000000/P0000000/0PPPPPPP/RNBQKBNR w KQkq - 0 1",
        )

        board.move(2**16, 2**8)
        self.assertEqual(
            board.FEN,
            "rnbqkbnr/pppppppp/00000000/00000000/00000000/00000000/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        )

        board.undo_move()
        self.assertEqual(
            board.FEN,
            "rnbqkbnr/pppppppp/00000000/00000000/00000000/P0000000/0PPPPPPP/RNBQKBNR w KQkq - 0 1",
        )

        board.move(2**14, 2**54)
        board.undo_move()
        self.assertEqual(
            board.FEN,
            "rnbqkbnr/pppppppp/00000000/00000000/00000000/P0000000/0PPPPPPP/RNBQKBNR w KQkq - 0 1",
        )

    @patch("chessengine.bitboard.Board.move_san")
    @patch("chessengine.bitboard.Board.get_input")
    def test_handle_player_move(self, mock_input, mock_move_san):
        mock_input.return_value = "a2a3"

        board = Board("white")
        move, lines_added, move_undone = board.handle_player_move("white", "")

        self.assertEqual(move, "a2a3")
        self.assertEqual(lines_added, 2)
        self.assertFalse(move_undone)
        mock_move_san.assert_called_with(move=move, side="white")

    @patch("chessengine.bitboard.Board.undo_move")
    @patch("chessengine.bitboard.Board.move_san")
    @patch("chessengine.bitboard.Board.get_input")
    def test_handle_player_move__undo(self, mock_input, mock_move_san, mock_undo):
        mock_input.return_value = "u"

        board = Board("white")
        move, lines_added, move_undone = board.handle_player_move("white", "")

        self.assertEqual(move, "u")
        self.assertEqual(lines_added, 2)
        self.assertTrue(move_undone)
        mock_move_san.assert_not_called()
        mock_undo.assert_called()

    @patch("chessengine.bitboard.Board.undo_move")
    @patch("chessengine.bitboard.Board.move_san")
    @patch("chessengine.bitboard.Board.get_input")
    def test_handle_player_move__undo_with_no_moves(
        self, mock_input, mock_move_san, mock_undo
    ):
        mock_input.return_value = "u"
        mock_undo.side_effect = RuntimeError("No moves have been made yet to undo.")

        board = Board("white")
        move, lines_added, move_undone = board.handle_player_move("white", "")

        self.assertEqual(move, "u")
        self.assertEqual(lines_added, 3)
        self.assertTrue(move_undone)
        mock_move_san.assert_not_called()
        mock_undo.assert_called()


if __name__ == "__main__":
    unittest.main()
