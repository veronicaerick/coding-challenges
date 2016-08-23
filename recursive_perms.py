def get_permutations(string):
    if len(string) <= 1:
        return string

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    permutations = get_permutations(all_chars_except_last)
    perms = set()

    for permutations