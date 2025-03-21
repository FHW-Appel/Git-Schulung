import random

def draw_lottery_numbers():
    """Erzeugt 6 zufällige Lottozahlen zwischen 1 und 49."""
    return random.sample(range(1, 50), 6)

def check_results(user_numbers, drawn_numbers):
    """Vergleicht die Benutzereingabe mit der Ziehung und gibt die Anzahl der Treffer zurück."""
    matched_numbers = set(user_numbers) & set(drawn_numbers)
    return len(matched_numbers), matched_numbers
