def is_permutation(word1, word2):
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    for i in range(len(sorted_word1)):
        if sorted_word1[i] != sorted_word2:
            return False

    return True 

