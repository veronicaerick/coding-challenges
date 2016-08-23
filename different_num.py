# #  Getting a Different Number
#  *
#  * Given an array arr of n unique non-negative integers, how can you most
#  * efficiently find a non-negative integer that is not in the array?
#  *
#  * Your solution should return such an integer or null if arr contains all
#  * possible integers.

def diff_num(array):
    # check to see if array is empty
    if len(array) < 1:
        return None 

    # start a dict of all nums we see in array
    seen = {}
    length = len(array)
    for i in range(len(array)):
        seen[i] = 1
    
    # see if anything else is in the dict
    different = 0
    while different < len(length):
        for key in seen.keys():
            if different != key:
                return different

