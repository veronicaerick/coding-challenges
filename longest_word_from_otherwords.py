def longest_word(words):
    words.sort(key=len, reverse = True)
    w_set = set(words)

    for w in words:
        for i in range(1, len(words)):
            left = w[:i]
            right = w [i:]

            if left in w_set and right in w_set:
                return w

def is_rotation(s1, s2):
    for i in range(len(s1)):
        if s1 == s2:
            return True

        s2 = s2[1:] + s2[0]

def rotate_array(lst, n):
    if n == 0:
        return lst
    elif n > len(lst):
        return lst[n-len(lst):] + lst[:n-len(lst)]
    else:
        return lst[n:] + lst[:n]

def permutations(string):
    perms = []
    first_char = string[0]
    get_perms = permutations(string[1:])

    for perm in get_perms:
        for i in range(len(perm) +1):
            perms.append(string[i:] + first_char + string[:i])