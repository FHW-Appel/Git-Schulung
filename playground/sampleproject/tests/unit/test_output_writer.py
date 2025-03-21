import unittest
from unittest.mock import patch
from output_writer import OutputWriter

class TestOutputWriter(unittest.TestCase):

    @patch("builtins.print")
    def test_write_results(self, mock_print):
        """Testet, ob die Methode die erwarteten Werte ausgibt."""
        writer = OutputWriter()

        tipp = [1, 2, 3, 4, 5, 6]
        game = [7, 8, 9, 10, 11, 12]
        result = "Treffer: 0"
        header = "### Lottoziehung ###"
        footer = "### Ende ###"

        writer.write_results(tipp, game, result, header, footer)

        # Prüft, ob print() mit den erwarteten Werten aufgerufen wurde
        mock_print.assert_any_call(header)
        mock_print.assert_any_call(tipp)
        mock_print.assert_any_call(game)
        mock_print.assert_any_call(result)
        mock_print.assert_any_call(footer)

if __name__ == "__main__":
    unittest.main()
