def pig_latin(string):
    vowels = ["a", "e", "i", "o", "u"]
    words = string.split()

    pig_latin_words = []
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word[1:] + "yay" + word[0])
        else:
           pig_latin_words.append(word + "ay")

    return " ".join(pig_latin_words)
