import unittest
from unittest.mock import patch
from input_reader import InputReader


class TestInputReader(unittest.TestCase):
    @patch("builtins.input", side_effect=["1 2 3 4 5 6"])
    def test_read_numbers(self, mock_input):
        """Testet, ob InputReader eine korrekt eingegebene Zahlensequenz liest."""
        reader = InputReader()
        self.assertEqual(reader.read_numbers(), ["1", "2", "3", "4", "5", "6"])

if __name__ == "__main__":
    unittest.main()


