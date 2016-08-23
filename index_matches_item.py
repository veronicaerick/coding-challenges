
# /*
#  * Array Index & Element Equality
#  *
#  * Given an array of sorted distinct integers named arr, write a function that
#  * returns an index i in arr for which arr[i] = i or -1 if no such index exists.
#  *
#  * Implement the most efficient solution possible, prove the correctness of your * solution and analyze its runtime complexity (in terms of n - the length of
#  * arr).
#  *
#  * Examples:
#  *
#  *   1. Given arr = [-8,0,2,5] the function returns 2, since arr[2] = 2
#  *
#  *   2. Given arr = [-1,0,3,6] the function returns -1, since no index in arr
#  *      satisfies arr[i] = i
#  */

def find_equality(array):
    start = 0
    end = array[-1]

    while start < end:
        middle = int(len(array)/2)
        if arr[middle] == middle:
            return middle
        elif arr[middle] < middle:
            start = middle + 1
        else:
            end = middle - 1;

    return -1;