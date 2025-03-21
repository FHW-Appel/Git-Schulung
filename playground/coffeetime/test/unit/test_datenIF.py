import unittest
import pandas as pd
from datenIF import TrinkDatenIF

class TestTrinkDatenIF(unittest.TestCase):

    def setUp(self):
        self.trinkdaten = TrinkDatenIF()

    def test_initial_dataframe(self):
        self.assertTrue(self.trinkdaten.trinkdaten.empty)
        self.assertListEqual(list(self.trinkdaten.trinkdaten.columns), ["Trinker", "Uhrzeit", "Getränk"])

    def test_zeile_hinzufuegen(self):
        self.trinkdaten.zeile_hinzufuegen("Alice", "08:00", "Kaffee")
        self.assertEqual(len(self.trinkdaten.trinkdaten), 1)
        self.assertEqual(self.trinkdaten.trinkdaten.iloc[0]["Trinker"], "Alice")
        self.assertEqual(self.trinkdaten.trinkdaten.iloc[0]["Uhrzeit"], "08:00")
        self.assertEqual(self.trinkdaten.trinkdaten.iloc[0]["Getränk"], "Kaffee")

    def test_dataframe_exportieren(self):
        self.trinkdaten.zeile_hinzufuegen("Alice", "08:00", "Kaffee")
        self.trinkdaten.dataframe_exportieren("test_trinkdaten.csv")
        df = pd.read_csv("test_trinkdaten.csv")
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Trinker"], "Alice")
        self.assertEqual(df.iloc[0]["Uhrzeit"], "08:00")
        self.assertEqual(df.iloc[0]["Getränk"], "Kaffee")

    def test_dataframe_einlesen(self):
        self.trinkdaten.zeile_hinzufuegen("Alice", "08:00", "Kaffee")
        self.trinkdaten.dataframe_exportieren("test_trinkdaten.csv")
        new_trinkdaten = TrinkDatenIF()
        new_trinkdaten.dataframe_einlesen("test_trinkdaten.csv")
        self.assertEqual(len(new_trinkdaten.trinkdaten), 1)
        self.assertEqual(new_trinkdaten.trinkdaten.iloc[0]["Trinker"], "Alice")
        self.assertEqual(new_trinkdaten.trinkdaten.iloc[0]["Uhrzeit"], "08:00")
        self.assertEqual(new_trinkdaten.trinkdaten.iloc[0]["Getränk"], "Kaffee")

if __name__ == '__main__':
    unittest.main()