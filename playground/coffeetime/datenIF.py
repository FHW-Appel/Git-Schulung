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

# Beispiel für die Verwendung der Klasse
if __name__ == "__main__":
    # Instanz der Klasse erstellen
    trinkdaten = TrinkDatenIF()
    
    # Zeilen hinzufügen
    trinkdaten.zeile_hinzufuegen("Alice", "08:00", "Kaffee")
    trinkdaten.zeile_hinzufuegen("Bob", "12:00", "Tee")
    
    # DataFrame ausgeben
    trinkdaten.dataframe_ausgeben()