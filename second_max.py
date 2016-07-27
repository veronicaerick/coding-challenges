def second_max(array):
    if len(array) < 2:
        return none

    max_num = array[0]
    second_max = min(array[0])

    for num in array:
        if num > max_num:
            max_num = num
            second_max = max_num

        elif num > second_max and num != max_num:
            second_max = num

    return second_max
            
