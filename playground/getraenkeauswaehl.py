def laden_getraenke(dateiname):
    try:
        with open(dateiname, 'r') as file:
            getraenke = file.readlines()
        return [getraenk.strip() for getraenk in getraenke]
    except FileNotFoundError:
        print("Die Datei 'getraenkenliste.txt' wurde nicht gefunden.")
        return []

def zeigen_getraenke(getraenke):
    print("Bitte wähle ein Getränk aus der Liste:")
    for getraenk in getraenke:
        print(getraenk)

def main():
    getraenke = laden_getraenke("getraenkenliste.txt")
    
    if not getraenke:
        return

    zeigen_getraenke(getraenke)

    try:
        auswahl = int(input("Geben Sie die Nummer des gewünschten Getränks ein: "))
        if 1 <= auswahl <= len(getraenke):
            print(f"Ihr gewähltes Getränk: {getraenke[auswahl - 1]}")
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Nummer aus der Liste.")
    except ValueError:
        print("Bitte geben Sie eine gültige Nummer ein.")

if __name__ == "__main__":
    main()