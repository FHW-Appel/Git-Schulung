#!/usr/bin/env python3

import time
import tkinter as tk

def show_coffee_cup():
    root = tk.Tk()
    root.title("Kaffeepause")
    label = tk.Label(root, text="☕", font=("Helvetica", 100))
    label.pack()
    
    def on_key(event):
        if event.char.lower() == 'k':
            root.destroy()
    
    root.bind("<Key>", on_key)
    root.mainloop()

def main():
    sip_number = 1
    while True:
        time.sleep(120)  # Warte 2 Minuten
        print(f"TRINK! Schluck Nummer: {sip_number}")
        show_coffee_cup()
        sip_number += 1

if __name__ == "__main__":
    main()