from is_palindrome import is_palindrome

def longest_pal_substring(string):
    if len(string) == 1:
        return string

    max_pal = ''
    max_len = 0

    for i in range(len(string)):
        for j in range(i +1, len(string)):
            if is_palindrome(string[i:j]) and j-i > max_len and j+1-i != 1:
                max_pal = string[i:j+1]
                max_len = j + 1 -i

    return max_pal