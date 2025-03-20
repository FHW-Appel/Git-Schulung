import unittest
from unittest.mock import patch, MagicMock
import main
import input_handler
import lottery
import output_handler
import output_writer
import sys

class TestIntegrationMain(unittest.TestCase):

    @patch("builtins.input", side_effect=["1 2 3 4 5 6"])
    @patch("lottery.draw_lottery_numbers", return_value=[10, 20, 30, 40, 41, 42])
    @patch("output_handler.print_results")
    @patch("output_writer.OutputWriter")  # Patch OutputWriter als Ganzes
    @patch("sys.stdout")  # Fängt Konsolenausgabe ab
    def test_main_execution(self, mock_stdout, mock_output_writer, mock_print_results, mock_draw, mock_input):
        """Integrationstest: Überprüft den vollständigen Ablauf der Lottoziehung und unterdrückt Konsolenausgabe."""

        # Erstelle Mock-Objekt für den Writer
        mock_writer = MagicMock()
        mock_output_writer.return_value = mock_writer  # Ersetzt OutputWriter durch Mock

        # Mock für get_user_numbers, um kontrollierte Eingaben zu simulieren
        with patch("input_handler.get_user_numbers", return_value=[1, 2, 3, 4, 5, 6]):
            main.main()

        # Überprüfen, ob die Zahlenziehung genau einmal aufgerufen wurde
        mock_draw.assert_called_once()

        # Überprüfen, ob die Ergebnisse korrekt an print_results übergeben wurden
        mock_print_results.assert_called_once_with(
            mock_writer, 
            [1, 2, 3, 4, 5, 6], 
            [10, 20, 30, 40, 41, 42], 
            0,  # Keine Treffer in diesem Szenario
            set()
        )

        # Überprüfen, ob die Ausgabe korrekt abgefangen wurde (kein Sonderzeichen)
        captured_output = mock_stdout.getvalue()
        self.assertNotIn("�", captured_output, "Fehler: Unerwartetes Zeichen in der Konsolenausgabe!")

if __name__ == "__main__":
    unittest.main()

