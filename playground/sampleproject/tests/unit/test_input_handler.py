import unittest
from input_handler import get_user_numbers

class MockReader:
    """Mock-Klasse für InputReader, um Testeingaben zu simulieren."""
    def __init__(self, numbers):
        self.numbers = numbers

    def read_numbers(self):
        return self.numbers

class TestInputHandler(unittest.TestCase):

    def test_valid_input(self):
        """Testet eine korrekte Eingabe."""
        reader = MockReader(["1", "2", "3", "4", "5", "6"])
        self.assertEqual(get_user_numbers(reader), [1, 2, 3, 4, 5, 6])

    def test_not_enough_numbers(self):
        """Testet, ob eine Eingabe mit zu wenigen Zahlen fehlschlägt."""
        reader = MockReader(["1", "2", "3", "4", "5"])
        with self.assertRaises(ValueError):
            get_user_numbers(reader)

    def test_non_numeric_input(self):
        """Testet, ob nicht-numerische Eingaben abgefangen werden."""
        reader = MockReader(["1", "2", "drei", "4", "5", "6"])
        with self.assertRaises(ValueError):
            get_user_numbers(reader)

    def test_numbers_out_of_range(self):
        """Testet Zahlen außerhalb des erlaubten Bereichs."""
        reader = MockReader(["0", "2", "3", "4", "5", "50"])
        with self.assertRaises(ValueError):
            get_user_numbers(reader)

    def test_duplicate_numbers(self):
        """Testet doppelte Eingaben."""
        reader = MockReader(["1", "2", "3", "3", "5", "6"])
        with self.assertRaises(ValueError):
            get_user_numbers(reader)

if __name__ == "__main__":
    unittest.main()
