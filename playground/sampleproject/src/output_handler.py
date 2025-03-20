def print_results(output_writer, user_numbers, drawn_numbers, matches, matched_numbers):
    """Gibt die Ziehungsergebnisse und Treffer aus."""
    output_writer.write_results(
        f"Deine Zahlen: {sorted(user_numbers)}",
        f"Gezogene Zahlen: {sorted(drawn_numbers)}",
        f"Treffer: {matches} ({sorted(matched_numbers)})" if matches > 0 else "Leider kein Treffer.",
        header="🔹 Lottoziehung abgeschlossen!🔹",
        footer="🎉 Viel Glück für die nächste Ziehung! 🎉")
       
    
