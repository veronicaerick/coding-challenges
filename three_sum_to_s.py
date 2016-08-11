def three_sum(array, s):
    int_dict = {}
    int_set = set(array)

    for i in enumerate(array):
        int_dict.setdefault(num, []).append(i)

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            diff = array[i] + array[j]
            if s - diff in int_set:
                return i, j, int_dict[s- diff][0]
