class OutputWriter:
    def write_results(self, tipp, game, result, header=None, footer=None):
        """Gibt die Ergebnisse aus."""
        if header:
            print(header)
        print(tipp)
        print(game)
        print(result)
        if footer:
            print(footer)