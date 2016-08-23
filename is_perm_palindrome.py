def is_perm_a_palindrome(string):
    # track chars we have only seen once
    uncoupled = set()

    for char in string:
        if char in uncoupled:
            uncoupled.remove(char)
        else:
            uncoupled.add(char)

    return len(uncoupled) <=1