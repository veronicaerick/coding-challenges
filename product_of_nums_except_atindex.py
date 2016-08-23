def get_products_of_ints_except_index(lst):
    # loop through and multiply all items except if 
    # item index == nested_index:
    products_of_ints_except_index = [None] * len(lst)
    # keep track of all products before index
    products_so_far = 1
    i = 0
    while i < len(lst):
        products_of_ints_except_index[i] = products_so_far
        products_so_far *= lst[i]
        i += 1
    products_so_far = 1
    while i > 0:
        products_of_ints_except_index[i] *= products_so_far
        products_so_far *= lst[i]
        i -= 1