

def encode(plain_text):
    plain_text = plain_text.lower()
    result = []
    
    for char in plain_text:
        if char.isalpha():  # Buchstaben spiegeln
            result.append(chr(ord('a') + (25 - (ord(char) - ord('a')))))
        elif char.isdigit():  # Zahlen unverändert
            result.append(char)
        # Satzzeichen und Leerzeichen ignorieren

    # Ergebnis in Gruppen zu 5 Zeichen aufteilen
    grouped = []
    for i in range(0, len(result), 5):
        grouped.append("".join(result[i:i+5]))
    
    return " ".join(grouped)


def decode(cipher_text):
    cipher_text = cipher_text.lower()
    result = []
    
    for char in cipher_text:
        if char.isalpha():  # Buchstaben spiegeln
            result.append(chr(ord('a') + (25 - (ord(char) - ord('a')))))
        elif char.isdigit():  # Zahlen unverändert
            result.append(char)
        # Leerzeichen und andere Zeichen ignorieren

    return "".join(result)



