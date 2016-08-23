def element_in_thing(needle,haystack):
    for hay in haystack:
        if needle in hay:
            return True

def needle_in_haystack1(needle, haystack):
    for i, hay in enumerate(haystack):
        if needle in hay:
            return x


def needle_in_haystack(needle, haystack):
    n_len = len(needle)

    for hay in haystack:
        if haystack(hay) + n_len <= len(haystack):
            if haystack[haystack.index(hay):n_len == needle]:
                return True
        else:
            if haystack[-n_len] == needle:
                return True

    return False