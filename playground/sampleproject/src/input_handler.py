def get_user_numbers(reader):
    """Verwendet einen Reader, um die Zahlenquelle zu bestimmen und validiert die Eingabe."""
    user_numbers = reader.read_numbers()
    
    # Validierung der Eingabe
    if not isinstance(user_numbers, list):
        raise ValueError("Fehler: Die Eingabe muss eine Liste sein.")
    
    if len(user_numbers) != 6:
        raise ValueError("Fehler: Es müssen genau 6 Zahlen eingegeben werden.")
    
    try:
        user_numbers = [int(num) for num in user_numbers]  # Konvertiere alle Zahlen
    except ValueError:
        raise ValueError("Fehler: Alle Werte müssen ganze Zahlen sein.")

    if not all(1 <= num <= 49 for num in user_numbers):
        raise ValueError("Fehler: Alle Zahlen müssen zwischen 1 und 49 liegen.")

    if len(set(user_numbers)) != 6:
        raise ValueError("Fehler: Keine doppelten Zahlen erlaubt.")

    return user_numbers
