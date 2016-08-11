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

def anagram_buckets(words):
    word_dict = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]

        out = []

        for srt_wrd, w in word_dict.iteritems():
            out.append(w)

        return out

# create a dictionary, sort each word in words. start a key:value pair for each
# sorted word. If word is in dict, append the word as a value. If not,
# add the word as the beginning value.

# break apart the sorted word and word and append the word to results
