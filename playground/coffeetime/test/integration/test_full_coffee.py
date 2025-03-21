import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import datenIF
import kaffeebohne_waehlen
import main


class TestKaffeeApp(unittest.TestCase):

    @patch('main.input', side_effect=["1", "Max", "Espresso", "5"])  # Simuliert Eingaben
    @patch('main.kaffeebohne_waehlen.main', return_value="Espresso")  # Simuliert Kaffeeauswahl
    @patch('main.datenIF.TrinkDatenIF')
    def test_neue_eingabe_hinzufuegen(self, mock_trinkdaten, mock_kaffeebohne, mock_input):
        # Mock für TrinkDatenIF
        mock_instance = mock_trinkdaten.return_value
        mock_instance.zeile_hinzufuegen = MagicMock()

        # Programm ausführen
        with patch('builtins.print') as mock_print:
            with self.assertRaises(SystemExit):  # Beendet nach Option 5
                main.clear_console = MagicMock()  # Verhindert Konsolenlöschung
                main.trinkdaten = mock_instance
                main.input = mock_input
                main.kaffeebohne_waehlen.main = mock_kaffeebohne

        # Überprüfen, ob die Methode zum Hinzufügen aufgerufen wurde
        mock_instance.zeile_hinzufuegen.assert_called_once_with("Max", unittest.mock.ANY, "Espresso")
        mock_print.assert_any_call("Eintrag hinzugefügt!")
        mock_print.assert_any_call("TRINK!")

    @patch('main.input', side_effect=["2", "5"])  # Simuliert Eingaben
    @patch('main.datenIF.TrinkDatenIF')
    def test_daten_anzeigen(self, mock_trinkdaten, mock_input):
        # Mock für TrinkDatenIF
        mock_instance = mock_trinkdaten.return_value
        mock_instance.dataframe_ausgeben = MagicMock()

        # Programm ausführen
        with patch('builtins.print') as mock_print:
            with self.assertRaises(SystemExit):  # Beendet nach Option 5
                main.clear_console = MagicMock()  # Verhindert Konsolenlöschung
                main.trinkdaten = mock_instance
                main.input = mock_input

        # Überprüfen, ob die Methode zum Anzeigen aufgerufen wurde
        mock_instance.dataframe_ausgeben.assert_called_once()
        mock_print.assert_any_call("\nAktuelle Trinkdaten:")

    @patch('main.input', side_effect=["3", "5"])  # Simuliert Eingaben
    @patch('main.datenIF.TrinkDatenIF')
    def test_daten_speichern(self, mock_trinkdaten, mock_input):
        # Mock für TrinkDatenIF
        mock_instance = mock_trinkdaten.return_value
        mock_instance.dataframe_exportieren = MagicMock()

        # Programm ausführen
        with patch('builtins.print') as mock_print:
            with self.assertRaises(SystemExit):  # Beendet nach Option 5
                main.clear_console = MagicMock()  # Verhindert Konsolenlöschung
                main.trinkdaten = mock_instance
                main.input = mock_input

        # Überprüfen, ob die Methode zum Speichern aufgerufen wurde
        mock_instance.dataframe_exportieren.assert_called_once_with("trinkdaten.csv")

    @patch('main.input', side_effect=["4", "5"])  # Simuliert Eingaben
    @patch('main.datenIF.TrinkDatenIF')
    def test_daten_laden(self, mock_trinkdaten, mock_input):
        # Mock für TrinkDatenIF
        mock_instance = mock_trinkdaten.return_value
        mock_instance.dataframe_einlesen = MagicMock()

        # Programm ausführen
        with patch('builtins.print') as mock_print:
            with self.assertRaises(SystemExit):  # Beendet nach Option 5
                main.clear_console = MagicMock()  # Verhindert Konsolenlöschung
                main.trinkdaten = mock_instance
                main.input = mock_input

        # Überprüfen, ob die Methode zum Laden aufgerufen wurde
        mock_instance.dataframe_einlesen.assert_called_once_with("trinkdaten.csv")

    @patch('main.input', side_effect=["5"])  # Simuliert Eingaben
    def test_programm_beenden(self, mock_input):
        # Programm ausführen
        with patch('builtins.print') as mock_print:
            with self.assertRaises(SystemExit):  # Beendet nach Option 5
                main.clear_console = MagicMock()  # Verhindert Konsolenlöschung
                main.input = mock_input

        # Überprüfen, ob die Beenden-Nachricht ausgegeben wurde
        mock_print.assert_any_call("Programm wird beendet. Auf Wiedersehen!")


if __name__ == "__main__":
    unittest.main()