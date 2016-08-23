# given an usorted array find a subarray which 
# adds to a target number
# naieve method runtime O(n2)
def sub_sum_to_target(array, target):
    # iterate through the array
    for i in range(len(array)):
        total = 0
        # iterate through again from i to the end
        for j in range(i, len(array)):
            # keep track of total by adding item at each pass
            total += array[j]
            # if total is the target, return that chunk
            if total == target:
                return array[i:j]+1
            if total > target:
                break

