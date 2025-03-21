#!/usr/bin/env python3

import kaffeebohne_waehlen as kaffeebohne_waehlen 
import datenIF as datenIF
from datetime import datetime  # Import für die aktuelle Uhrzeit
import os

def clear_console():
    '''Löscht die Konsolenausgabe.'''
    os.system('cls' if os.name == 'nt' else 'clear')

print("Willkommen zur Kaffee-Erinnerungs-App!")

# Instanz der Klasse erstellen
trinkdaten = datenIF.TrinkDatenIF()

clear_console()
while True:
    print("\nWas möchten Sie tun?")
    print("1: Neue Eingabe hinzufügen")
    print("2: Daten anzeigen")
    print("3: Daten speichern")
    print("4: Daten laden")
    print("5: Programm beenden")
    
    auswahl = input("Bitte wählen Sie eine Option (1/2/3): ")
    
    if auswahl == "1":
        clear_console()
        # Neue Eingabe hinzufügen
        trinker = input("Name des Trinkers: ")
        uhrzeit = datetime.now().strftime("%H:%M")  # Aktuelle Uhrzeit im Format HH:MM
        getraenk = kaffeebohne_waehlen.main()
        trinkdaten.zeile_hinzufuegen(trinker, uhrzeit, getraenk)
        print("Eintrag hinzugefügt!")
        print("TRINK!")
    elif auswahl == "2":
        # Daten anzeigen
        clear_console()
        print("\nAktuelle Trinkdaten:")
        trinkdaten.dataframe_ausgeben()
    elif auswahl == "3":
        # Daten speichern
        clear_console()
        trinkdaten.dataframe_exportieren("trinkdaten.csv")
    elif auswahl == "4":
        # Daten laden
        clear_console()
        trinkdaten.dataframe_einlesen("trinkdaten.csv")
    elif auswahl == "5":
        # Programm beenden
        clear_console()
        print("Programm wird beendet. Auf Wiedersehen!")
        break
    else:
        print("Ungültige Eingabe. Bitte wählen Sie 1, 2 oder 3.")



exit(0)








