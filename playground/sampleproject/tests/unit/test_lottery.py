import unittest
from unittest.mock import patch
from lottery import draw_lottery_numbers, check_results

class TestLottery(unittest.TestCase):

    @patch("random.sample", return_value=[3, 7, 12, 25, 36, 49])
    def test_draw_lottery_numbers(self, mock_sample):
        """Testet, ob draw_lottery_numbers eine Liste mit 6 einzigartigen Zahlen im Bereich 1-49 zurückgibt."""
        numbers = draw_lottery_numbers()
        self.assertEqual(numbers, [3, 7, 12, 25, 36, 49])  # Da `random.sample` gemockt ist, sollte genau das rauskommen.
        self.assertEqual(len(numbers), 6)  # Muss genau 6 Zahlen enthalten
        self.assertTrue(all(1 <= num <= 49 for num in numbers))  # Alle Zahlen müssen im Bereich 1-49 sein
        self.assertEqual(len(set(numbers)), 6)  # Keine doppelten Zahlen

    def test_check_results_no_match(self):
        """Testet check_results, wenn keine Übereinstimmung vorliegt."""
        user_numbers = [1, 2, 3, 4, 5, 6]
        drawn_numbers = [10, 20, 30, 40, 41, 42]
        matches, matched_numbers = check_results(user_numbers, drawn_numbers)
        self.assertEqual(matches, 0)
        self.assertEqual(matched_numbers, set())

    def test_check_results_some_matches(self):
        """Testet check_results, wenn es einige Übereinstimmungen gibt."""
        user_numbers = [1, 2, 3, 4, 5, 6]
        drawn_numbers = [3, 4, 15, 25, 35, 45]
        matches, matched_numbers = check_results(user_numbers, drawn_numbers)
        self.assertEqual(matches, 2)
        self.assertEqual(matched_numbers, {3, 4})

    def test_check_results_all_matches(self):
        """Testet check_results, wenn alle 6 Zahlen übereinstimmen (Jackpot)."""
        user_numbers = [5, 10, 15, 20, 25, 30]
        drawn_numbers = [5, 10, 15, 20, 25, 30]
        matches, matched_numbers = check_results(user_numbers, drawn_numbers)
        self.assertEqual(matches, 6)
        self.assertEqual(matched_numbers, {5, 10, 15, 20, 25, 30})

if __name__ == "__main__":
    unittest.main()
