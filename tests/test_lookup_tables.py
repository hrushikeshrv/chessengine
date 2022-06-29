import unittest
from src.lookup_tables import lsb_pos


class TestLookupTables(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
