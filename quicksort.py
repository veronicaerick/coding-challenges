def quicksort(array):
    pivot = array[0]
    less = quicksort([x for x in array[1:] if x < pivot])
    greater = quicksort([x for x in array[1:] ix x => pivot])

    return less + pivot + greater