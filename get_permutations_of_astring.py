def get_permutations(word):
    output = []
    permutations = get_permutations(word[1:])
    first_char = word[0]

    for perm in permutations:
        for i in range(len(perm) + 1):
            output.append(perm[:i] + first_char + perm[i:])

    return output


