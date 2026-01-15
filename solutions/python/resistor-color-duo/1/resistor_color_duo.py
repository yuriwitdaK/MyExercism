def color_code(color):
    colors = ['black', 'brown', 'red', 'orange', 'yellow',
              'green', 'blue', 'violet', 'grey', 'white']
    return colors.index(color)

def colors():
    return ['black', 'brown', 'red', 'orange', 'yellow',
            'green', 'blue', 'violet', 'grey', 'white']
def value(color_list):
    #had to rate it myself
    first = color_code(color_list[0])
    second = color_code(color_list[1])
    return first * 10 + second



def color_code(color):
    return colors().index(color)


def color_codes(color_list):
    return [color_code(c) for c in color_list]