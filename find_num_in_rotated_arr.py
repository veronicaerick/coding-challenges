# # 1. Find a given number num in a sorted array arr:
# arr = [2, 4, 5, 9, 12, 17] 

# 2. If the sorted array arr is shifted left by 
# an unknown offset and you don't have a pre-shifted 
# copy of it, how would you modify your method to find a 
# number in the shifted array?
# shiftArr = [9, 12, 17, 2, 4, 5]

# Explain and code an efficient solution and analyze 
# its runtime complexity
# if num doesn't exist in the array, return -1

def binary_search(num, arr):
    start = arr[0]
    end = arr[-1]
    while start <= end:
        middle = (start + end)/2
        if arr[mid] < num:
            begin = middle + 1
        elif arr[mid] > num:
            end = middle - 1
        else:
            return middle

    return -1

def shifted_arr_search(num, arr):
    original_first = get_original_first(arr)
    if num => arr[0]:
        shift_arr = arr(0, original_first)
        return binary_search(num, arr)
    else:
        n = length(arr)
        shift_arr = arr(original_first -1, n -1)
        return binary_search(num, arr)


def get_original_first(arr):
    start = 0
    end = len(arr)
    while start <= end:
        mid = (begin + end)/2
        if mid == 0 or arr[mid] < arr[mid-1]:
            return mid
        if arr[mid] > arr[0]:
            start = mid + 1
        else: 
            end = mid - 1