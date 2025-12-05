def translate(text):
    words = text.split()
    return " ".join(translate_word(w) for w in words)


def translate_word(word):
    vowels = ("a", "e", "i", "o", "u")

    #exception: Wörter, die wie VOKALE behandelt werden:
    if word.startswith(("xr", "yt")):
        return word + "ay"

    # Wenn Wort mit einem Vokal beginnt → einfach "ay" anhängen
    if word[0] in vowels:
        return word + "ay"

    # Ansonsten: wir verschieben den Anfangs-Konsonantencluster
    index = 0
    length = len(word)

    # Sondercluster
    while index < length:
        # "qu" zählt als EIN Laut
        if word[index:index+2] == "qu":
            index += 2
        # andere Cluster (ch, thr, sch etc. werden automatisch abgedeckt)
        elif word[index] not in vowels and not (word[index] == "y" and index != 0):
            index += 1
        else:
            break

    return word[index:] + word[:index] + "ay"