# brute force :( O(n2))
def sub_sum_target(array, t):
    for i in range(len(array)):
        count = 0
        for j in range(i, len(array)):
            count += array[j]
            if count == t:
                return array[i:j+1]
            else:
                return None

def sub_sum_target_v2(array, t):
    total = array[0]
    start = 0

    for i in range(1,(len(array) + 1)):
        # if total is greater than t, remove it and move through
        while total > t and start < i -1:
            t = t - array[start]
            start += 1
        # when subarray reaches target, return that chunk
        if total == t:
            return array[start:i]
