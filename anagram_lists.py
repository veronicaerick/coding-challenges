def anagram_lists(words):
    word_dict = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]

    out = []

    for sortd_wrd, w in word_dict.iteritems():
        out.append(w)

    return out
