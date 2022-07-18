from src.utils import get_bit_positions

import unittest


class TestUtils(unittest.TestCase):
    def test_get_bit_positions(self):
        self.assertEqual(get_bit_positions(0b110100), [0b100, 0b10000, 0b100000])


if __name__ == '__main__':
    unittest.main()
