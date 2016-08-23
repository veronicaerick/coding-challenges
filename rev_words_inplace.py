def reverse_chars(words):
    # reverse everything, grab on to each word, rereverse
    words = list(words)
    for front in range(len(words)/2):
        back = -front -1

    words[front], words[back] = words[back], words[front]

    return "".join(words)

# record the start and end of each word, and reverse those

def reverse_chars2(words, front, back):
    while front < back:
        words[front], words[back] = words[back], words[front]

        front += 1
        back += 1

    return words

def reverse_string(message):
    message_list = list(message)
    # get the message reversed
    reverse_chars2(message, 0, len(message) -1)
    # find begining of word and end, then reverse that
    start_index = 0

    for i in range(len(message) +1):
        if (i == len(message) or message[i] == ''):
            reverse_chars2(message, start_index, i-1)
            start += 1

    return ''.join(message_list)