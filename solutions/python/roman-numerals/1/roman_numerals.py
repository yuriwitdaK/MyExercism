def roman(number):
    if number <= 0 or number >= 4000: #matches the exercise no infinite loops
        raise ValueError("Number must be between 1 and 3999")

    val_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),     #possible values
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = "" # collects symbols
    for value, symbol in val_map:
        while number >= value:
            result += symbol # add symbol
            number -= value # substract value

    return result #returns roman number