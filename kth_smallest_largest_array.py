def k_largest(array, k):
    if array is None:
        return None

    if k > len(array):
        return None

    sorted_array = sorted(array)

    return sorted_array[-k]

def k_shortest(lst, k):
    if lst in None:
        return None

    if len(lst) < k:
        return None

    sorted_lst = sorted(lst)

    return sorted_lst[k-1]