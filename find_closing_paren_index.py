def find_closer(string, open_paren_index):
    open_nested = 0
    position = open_nested + 1

    while position <= len(string) -1:
        char = string[position]

        if (char == ')'):
            if open_nested = 0:
                return position
            else:
                open_nested -= 1

        position += 1

    return False
