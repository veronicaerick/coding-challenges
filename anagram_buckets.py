def anagram_bucks(lst):
    word_dict = {}

    for word in lst:
        sorted_word = "".join(sorted(word))
        
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [w]

    results = []
    for sw, w in word_dict.iteritems():
        results.append(w)

    return results