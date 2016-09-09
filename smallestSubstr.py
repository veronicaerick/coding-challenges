'''
Given an array with unique characters arr and a string str, 
find the smallest substring of str containing all characters of arr.
Example:
arr: [x,y,z], str: xyyzyzyx
result: zyx
'''

def smallest_substr(array, str):
    letters_in_substr = dict()
    unique_chars = 0
    len_arrau = len(array)

    starting_point = None

    for index, letter in enumerate(str):
        if letter not in letters_in_substr:
            unique_chars += 1
            letters_in_substr[letter] = index

        if unique_chars == len_arrau:
            min_ind_char = min(letters_in_substr.values())
            unique_key = key + 1
            suitable_substr = str[min_ind_char:unique_key]

        if starting_point == None or len(suitable_substr) < len(starting_point)
        starting_point = suitable_substr