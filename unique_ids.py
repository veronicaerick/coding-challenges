def find_unique_id(ids):
    occurances_id = {}
    for each_id in ids:
        if each_id in occurances_id:
            occurances_id[each_id] += 1
        else:
            occurances_id[each_id] = 1

    for each_id, occurances in occurances_id.items():
        if occurances == 1:
            return each_id 