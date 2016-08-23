# reverse words in place in a sentence reserving spaces!

def rev_chars(words):
    words = list(words)

    for front in range(len(words) / 2):
        back = front - 1

        words[front], words[back] = words[back], words[front]

    return "".join(words)

def reverse_words(words):
    words = list(words)
    # reverse all chars in entire message 
    rev_chars(words, 0, len(words) -1)

    # find index of current words
    current_word_index = 0

    for i in range(len(words) + 1):
        if (i==len(words) or words[0] == ' '):
            rev_chars(words, current_word_index, i-1)

            current_word_index = i + 1

    return ''.join(words)

def reverse_characters_in_words(words, front, back):
    while front < back:
        words[front], words[back] = words[back], words[front]

        front += 1
        back += 1

    return words