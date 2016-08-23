def merge_liists(list1, list2):
    out_list = []
    i = 0 
    j = 0

    while len(i) < len(list1) and len(j) < len(list2):
        if list1[i] < list2[j]:
            out_list.append(list1[i])
            i += 1

        else:
            out_list.append(list2[j])
            j += 1

    out_list.extend(list1[i:])
    out_list.extend(list2[j:])

    return out_list