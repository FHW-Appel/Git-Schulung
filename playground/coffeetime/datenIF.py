import pandas as pd


class TrinkDatenIF:
    def __init__(self):
        '''Initialisiert ein Attribut, das ein leeres DataFrame mit den Spalten "Trinker", "Uhrzeit" und "Getränk" enthält.'''
        self.trinkdaten = pd.DataFrame(columns=["Trinker", "Uhrzeit", "Getränk"])

    def zeile_hinzufuegen(self, trinker, uhrzeit, getraenk):
        '''Fügt eine neue Zeile zum DataFrame hinzu.'''
        neue_zeile = {"Trinker": trinker, "Uhrzeit": uhrzeit, "Getränk": getraenk}
        # Hinzufügen der neuen Zeile mit loc
        self.trinkdaten.loc[len(self.trinkdaten)] = neue_zeile

    def dataframe_ausgeben(self):
        '''Gibt den aktuellen DataFrame in der Konsole aus.'''
        print(self.trinkdaten)
    
    def dataframe_exportieren(self, dateipfad):
        '''Exportiert den DataFrame in eine externe Datei (z. B. CSV).'''
        try:
            self.trinkdaten.to_csv(dateipfad, index=False, encoding='utf-8')
            print(f"DataFrame erfolgreich nach '{dateipfad}' exportiert.")
        except Exception as e:
            print(f"Fehler beim Exportieren des DataFrames: {e}")

# Beispiel für die Verwendung der Klasse
if __name__ == "__main__":
    # Instanz der Klasse erstellen
    trinkdaten = TrinkDatenIF()
    
    # Zeilen hinzufügen
    trinkdaten.zeile_hinzufuegen("Alice", "08:00", "Kaffee")
    trinkdaten.zeile_hinzufuegen("Bob", "12:00", "Tee")
    
    # DataFrame ausgeben
    trinkdaten.dataframe_ausgeben()

    # DataFrame exportieren
    trinkdaten.dataframe_exportieren("trinkdaten.csv")