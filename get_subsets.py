def get_subsets(array):
    result = []
    head = array[0]
    if len(array) < 0:
        return 0 
        
    for item in get_subsets(array[1:]):
        result.append(head + item)
        result.append(item)

    return result
