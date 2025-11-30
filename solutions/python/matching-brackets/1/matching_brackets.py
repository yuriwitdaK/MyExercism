def is_paired(input_string):
    stack = []
    opening = "([{"
    closing = ")]}"
    matches = {")": "(", "]": "[", "}": "{"}

    for char in input_string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()
    
    return len(stack) == 0