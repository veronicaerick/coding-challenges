def max_subarray(arr):
    # first element seen
    last_seen = arr[0]
    # assign max to what we're looking at
    max_sub = last_seen
    # iterate through from first index, if x is bigger that the last seen + x
    # last_seen becomes x otherwise add what were on to subarray
    for x in arr[1:]:
        if x > last_seen + x:
            last_seen = x
        else:
            last_seen += x
        # calculate max subarray by comparing
        max_sub = max(max_sub, last_seen)

    return max_sub
