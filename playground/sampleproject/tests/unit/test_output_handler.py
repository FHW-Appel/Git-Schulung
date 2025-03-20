import unittest
from unittest.mock import MagicMock
from output_handler import print_results

class TestPrintResults(unittest.TestCase):

    def test_print_results(self):
        """Testet, ob print_results die erwarteten Werte an OutputWriter weitergibt."""
        mock_writer = MagicMock()

        user_numbers = [6, 12, 18, 24, 30, 36]
        drawn_numbers = [5, 10, 15, 20, 25, 30]
        matches = 1
        matched_numbers = [30]

        print_results(mock_writer, user_numbers, drawn_numbers, matches, matched_numbers)

        # Erwartete Werte
        expected_tipp = f"Deine Zahlen: {sorted(user_numbers)}"
        expected_game = f"Gezogene Zahlen: {sorted(drawn_numbers)}"
        expected_result = f"Treffer: {matches} ({sorted(matched_numbers)})"
        expected_header = "🔹 Lottoziehung abgeschlossen!🔹"
        expected_footer = "🎉 Viel Glück für die nächste Ziehung! 🎉"

        # Prüfen, ob write_results mit den richtigen Werten aufgerufen wurde
        mock_writer.write_results.assert_called_once_with(
            expected_tipp, expected_game, expected_result, header=expected_header, footer=expected_footer
        )

if __name__ == "__main__":
    unittest.main()
