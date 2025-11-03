def color_code(color):
    colors = ['black', 'brown', 'red', 'orange', 'yellow',
              'green', 'blue', 'violet', 'grey', 'white']#list of the colors in order
    return colors.index(color)#usage of list and position in list with index

def colors():
    return ['black', 'brown', 'red', 'orange', 'yellow',
            'green', 'blue', 'violet', 'grey', 'white']


def color_code(color):
    return colors().index(color)


def color_codes(color_list):
    return [color_code(c) for c in color_list]#read position
