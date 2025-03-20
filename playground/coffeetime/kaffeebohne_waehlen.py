import os

ctr = 0

def waehlen(sortennummer, sortenliste):
    '''Gibt die gewählte Sorte aus.'''
    if 1 <= sortennummer <= len(sortenliste):
        print(f"Sie haben {sortenliste[sortennummer - 1]} gewählt.")
    else:
        print("Ungültige Auswahl.")

def auflistung(sortenliste):
    '''Gibt die Sortenliste aus.'''
    global ctr
    print('Wähle eine Sorte aus der Liste:')
    for s in sortenliste:
        ctr += 1
        print("\t \t \t \t", str(ctr), f"\t{s}")

def main():
    '''Hauptfunktion des Programms.'''
    # Einlesen der Sortenliste aus der Datei
    file_path = os.path.join(os.path.dirname(__file__), 'kaffeebohnen.txt')
    try:
        with open(file_path, 'r') as file:
            sortenliste = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
        return
    
    # Sortenliste ausgeben
    auflistung(sortenliste)
    
    # Nutzereingabe anfordern
    try:
        auswahl = int(input("Bitte geben Sie die Nummer der gewünschten Sorte ein: "))
        waehlen(auswahl, sortenliste)
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")

if __name__ == "__main__":
    '''Falls das Skript direkt ausgeführt wird, wird die main-Funktion aufgerufen.'''
    main()