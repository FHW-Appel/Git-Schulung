import unittest
from unittest.mock import patch, mock_open, call
import __init__
import kaffeebohne_waehlen

class TestKaffeebohneWaehlen(unittest.TestCase):

    def setUp(self):
        self.sortenliste = ["Arabica", "Canephora", "Liberica"]

    @patch('builtins.print')
    def test_waehlen_valid(self, mock_print):
        kaffeebohne_waehlen.waehlen(1, self.sortenliste)
        mock_print.assert_called_with("Sie haben Arabica gewählt.")

    @patch('builtins.print')
    def test_waehlen_invalid(self, mock_print):
        kaffeebohne_waehlen.waehlen(4, self.sortenliste)
        mock_print.assert_called_with("Ungültige Auswahl.")

    @patch('builtins.print')
    def test_auflistung(self, mock_print):
        kaffeebohne_waehlen.auflistung(self.sortenliste)
        expected_calls = [
            call('Wähle eine Sorte aus der Liste:'),
            call("\t \t \t \t", '1', "\tArabica"),
            call("\t \t \t \t", '2', "\tCanephora"),
            call("\t \t \t \t", '3', "\tLiberica")
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', return_value='1')
    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open, read_data="Arabica\nCanephora\nLiberica\n")
    def test_main_valid(self, mock_open, mock_print, mock_input):
        with patch('os.path.join', return_value='kaffeebohnen.txt'):
            result = kaffeebohne_waehlen.main()
            mock_print.assert_any_call("Sie haben Arabica gewählt.")
            self.assertEqual(result, {"Arabica"})

    @patch('builtins.input', return_value='invalid')
    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open, read_data="Arabica\nCanephora\nLiberica\n")
    def test_main_invalid_input(self, mock_open, mock_print, mock_input):
        with patch('os.path.join', return_value='kaffeebohnen.txt'):
            result = kaffeebohne_waehlen.main()
            mock_print.assert_any_call("Bitte geben Sie eine gültige Zahl ein.")
            self.assertIsNone(result)

    @patch('builtins.print')
    def test_main_file_not_found(self, mock_print):
        with patch('os.path.join', return_value='non_existent_file.txt'):
            result = kaffeebohne_waehlen.main()
            mock_print.assert_called_with("Die Datei non_existent_file.txt wurde nicht gefunden.")
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()