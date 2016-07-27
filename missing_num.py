def missing_num(array):
    if len(array) < 1:
        return None

    if array[0] != 1:
        return 1

    total = sum(range(array[-1] + 1)

    for num in array:
        total -= num

    if total == 0:
        return None

    return total  
