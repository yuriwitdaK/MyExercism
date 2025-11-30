def transform(legacy_data):
    new_data = {}

    # Schritt 1: Buchstaben mit Punktwerten verknüpfen
    for key, values in legacy_data.items():
        for val in values:
            new_data[val] = key

    # Schritt 2: Alle Buchstaben in Kleinbuchstaben umwandeln
    data = {str(k).lower(): v for k, v in new_data.items()}

    # Schritt 3: Fertiges Dictionary zurückgeben
    return data