def reverse_string(string):
    rev_string = ""

    for char in string:
        rev_string += char + rev_string

    return rev_string

def reverse_string_inplace(string):

    for i in range(len(string)/2):
        str_list[i], str_list[i-1] = str_list[i-1], str_list[i]

def get_subsets(elements):

    if len(elements) < 1:
        return None

    subsets = get_subsets(elements[1:])
    results = []

    for s in elements:
        results.append(elements[0] + s)
        results.append(s)

    return results
