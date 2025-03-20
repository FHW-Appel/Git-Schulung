from datetime import datetime, timedelta
import time

def zeit_bis_naechste_pause(pausenzeiten):
    """Berechnet die Zeit bis zur nächsten Pause"""
    jetzt = datetime.now()
    heute = jetzt.date()
    
    # Konvertiere Pausenzeiten in datetime-Objekte
    pause_zeiten = [datetime.strptime(p, "%H:%M").replace(year=jetzt.year, month=jetzt.month, day=jetzt.day) for p in pausenzeiten]
    
    # Finde die nächste Pause
    for pause in pause_zeiten:
        if pause > jetzt:
            return (pause - jetzt).seconds  # Rückgabe in Sekunden
    
    # Falls keine Pause mehr für heute übrig ist, nehme die erste Pause am nächsten Tag
    erste_pause_morgen = pause_zeiten[0] + timedelta(days=1)
    return (erste_pause_morgen - jetzt).seconds

def pausen_timer(pausenzeiten):
    """Timer-Funktion, die ständig die Zeit bis zur nächsten Pause überprüft."""
    while True:
        sekunden_bis_pause = zeit_bis_naechste_pause(pausenzeiten)
        minuten = sekunden_bis_pause // 60
        sekunden = sekunden_bis_pause % 60
        
        print(f"Nächste Pause in: {minuten} Minuten und {sekunden} Sekunden")
        
        time.sleep(30)  # Aktualisiere alle 30 Sekunden

# Beispiel-Pausenzeiten (kann angepasst werden)
pausen_liste = ["09:30", "12:00", "15:00", "18:30"]

# Starte den Timer
pausen_timer(pausen_liste)
