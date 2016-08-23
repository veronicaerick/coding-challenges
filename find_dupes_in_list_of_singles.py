def find_dup(lst):
    # start a set, add each int from list, if we 
    # pass an int that weve seen, return it 
    num_set = set()
    for num in lst:
        if num in num_set:
            return num 
        else:
            num_set.add(num)
