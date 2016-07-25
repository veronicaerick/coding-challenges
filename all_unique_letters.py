def all_unique_letters(word):
    """ 
    >>> all_unique_letters("apple")
    False
    >>> all_unique_letters("grape")
    True
    """

    unique_letters = set()

    for letter in word:
        if letter in unique_letters:
            return False
        unique_letters.append(letter)

    return True