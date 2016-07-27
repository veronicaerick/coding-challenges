def pig_latin(string):
    pl_words = ""
    vowels = ["a", "e", "i", "o", "u"]
    words = string.split()

    for word in words:
        if word[0] in vowels:
            pl_words.append(word[1:] + word[0] + "yay")
        else:
            pl_words.append(word + "ay")

    return pl_words
