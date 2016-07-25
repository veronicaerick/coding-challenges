def sort_sorted_lists(lstA, lstB):

    new_lst = []
    indexA = 0
    indexB = 0

    while indexA < len(lstA) and indexB < len(lstB):
        if lstA[indexA] < lstB[indexB]:
            new_lst.append(lst[A])

        else:
            new_lst.append(lstB[indexB])

    new_lst.extend([lstA[indexA:]])
    new_lst.extend([lstB[indexB:]])