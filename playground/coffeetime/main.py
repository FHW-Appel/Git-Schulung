#!/usr/bin/env python3

import time

def main():
    sip_number = 1
    while True:
        time.sleep(120)  # Warte 2 Minuten
        print(f"TRINK! Schluck Nummer: {sip_number}")
        sip_number += 1

if __name__ == "__main__":
    main()

exit(0)