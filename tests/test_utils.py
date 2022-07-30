from chessengine.utils import get_bit_positions, lsb_pos

import unittest


class TestUtils(unittest.TestCase):
    def test_get_bit_positions(self):
        self.assertEqual(get_bit_positions(0b110100), [0b100, 0b10000, 0b100000])
    
    def test_lsb_pos(self):
        test_cases = (
            (0b1010, 0b10),
            (0b1110010, 0b10),
            (0b1000010, 0b10),
            (0b1001, 0b1),
            (0b1, 0b1),
        )
        for arg, expected in test_cases:
            with self.subTest(arg=arg):
                self.assertEqual(lsb_pos(arg), expected)


if __name__ == '__main__':
    unittest.main()
