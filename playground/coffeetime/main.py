#!/usr/bin/env python3

import time
import winsound
from datetime import datetime

if __name__ == "__main__":
    
    print("Willkommen zur Kaffee-Erinnerungs-App!")
    middach = False

    while True:

        # Hole die aktuelle Uhrzeit
        current_time = datetime.now().strftime("%H:%M").split(":")
        
        if len(current_time) == 2:

            # Prüfe, ob es 12:00 Uhr ist
            if current_time[0] == "12" and int(current_time[1]) == 0 and middach == False:
                middach = True
                print("Middach!")
                winsound.Beep(2500, 1000) # Beep mit 2500Hz für 1 
            else:
                middach = False
                
        else:
            raise ValueError("Ungültige Uhrzeit")

        time.sleep(40)  # Für 40 Sekunden warten

exit(0)