def commands(b):
    b = b.zfill(5)  # sicherstellen, dass es 5 Bits hat
    actions = []

    if b[-1] == '1':
        actions.append("wink")
    if b[-2] == '1':
        actions.append("double blink")
    if b[-3] == '1':
        actions.append("close your eyes")
    if b[-4] == '1':
        actions.append("jump")
    if b[-5] == '1':
        actions.reverse()

    return actions
