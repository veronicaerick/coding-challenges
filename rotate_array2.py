def rotate_array(array, num):
    if num > len(array):
        rotate_by = num % len(array)
    else:
        rotate_by = num

    rotated_array = array[-rotate_by:] + array[:-rotate_by]

    return rotated_array