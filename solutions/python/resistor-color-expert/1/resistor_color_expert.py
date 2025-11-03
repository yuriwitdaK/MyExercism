color_values =['black','brown','red','orange','yellow','green','blue','violet','grey','white']

def resistor_label(colors):
    colors_values =['black','brown','red','orange','yellow','green','blue','violet','grey','white']
#turn colors to numbers so i can do math
    tolerance_values = {
        'grey': '±0.05%',
        'violet': '±0.1%',
        'blue': '±0.25%',
        'green': '±0.5%',
        'brown': '±1%',
        'red': '±2%',
        'gold': '±5%',
        'silver': '±10%'
    } # tolerance values

    if len(colors) == 1:
        value = color_values.index(colors[0])
        return f"{value} ohms"  #if only one resistor

    if len(colors) == 4:
        first = color_values.index(colors[0])
        second = color_values.index(colors[1])
        multiplier = 10 ** color_values.index(colors[2])
        tolerance = tolerance_values.get(colors[3], "")

        resistance = (first * 10 + second) * multiplier # if its a 4 color band

    elif len(colors) == 5:
        first = color_values.index(colors[0])
        second = color_values.index(colors[1])
        third = color_values.index(colors[2])
        multiplier = 10 ** color_values.index(colors[3])
        tolerance = tolerance_values.get(colors[4], "")

        resistance = (first * 100 + second * 10 + third) * multiplier

    if resistance >= 1_000_000_000:
        value_str = f"{resistance / 1_000_000_000:g} gigaohms"
    elif resistance >= 1_000_000:
        value_str = f"{resistance / 1_000_000:g} megaohms"
    elif resistance >= 1_000:
        value_str = f"{resistance / 1_000:g} kiloohms"
    else:
        value_str = f"{resistance} ohms"

    return f"{value_str} {tolerance}".strip()