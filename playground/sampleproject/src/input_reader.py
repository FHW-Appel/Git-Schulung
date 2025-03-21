class InputReader:
    """Standardmäßiger Reader für die Benutzereingabe über die Konsole."""
    
    def read_numbers(self):
        return input("Bitte gib 6 Zahlen zwischen 1 und 49 ein: ").split()