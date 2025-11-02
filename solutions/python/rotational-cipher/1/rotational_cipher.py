def rotate(text, key):
    result = ""
    for i,char in enumerate(text):# splits value in two, i=position,char=letter
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + key) % 26 + base)
            result += new_char
        else:
            result += char  #add numbers and all that back
    return result
