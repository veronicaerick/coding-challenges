def compress_string(string):
    seen_chars = string[0]
    char_counts = 1

    for i in range(1,len(string)):
        # if our what were seeing has been seen before and is
        # last item in list, add a count to
        # that char
        if string[i] == seen_chars[-1]:
            seen_chars[-1] += 1
        # if not seen yet, append the char to seen list and add one to char count
        else:
            seen_chars.append(string[i])
            char_counts.append(1)

        compression = ""
        # for each char and its count, put them into a tuple,
        # add the letter and num as a string to the compression
        for char, count in zip(seen_chars, char_counts):
            compression += char + str(count)

        # making sure to only return the compression if it actually compresses
        if len(compression) > len(string):
            return string

        return compression
