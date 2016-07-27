# rotate an array using the first element in the array for
# how many to rotate by

def rotate_array(arr):
    # grab by how many we wanna rotate by
    rotate_by = arr[0]
    # new array starting at that index to the end of list
    new_arr = arr[rotate_by:]
    # add that first chunk to the array from that number to the end
    new_arr = new_arr + arr[:rotate_by]
    # get results by joining together as a string, turning back into
    # a list of ints
    results = int("".join(map(str,new_arr)))

    return results
