def label(colors):
    color_values = ['black', 'brown', 'red', 'orange', 'yellow',
                    'green', 'blue', 'violet', 'grey', 'white']
    
    #main vlue (first two colors)
    main_value = color_values.index(colors[0]) * 10 + color_values.index(colors[1])
    
    #multiplier (third colour)
    multiplier = 10 ** color_values.index(colors[2])
    resistance = main_value * multiplier

    # turn in ohms
    if resistance >= 1_000_000_000:
        return f"{resistance // 1_000_000_000} gigaohms"
    elif resistance >= 1_000_000:
        return f"{resistance // 1_000_000} megaohms"
    elif resistance >= 1_000:
        return f"{resistance // 1_000} kiloohms"
    else:
        return f"{resistance} ohms"