# find the kth to last element, given the n and the head.
# count the nodes in the linked list, and then stop at the second to last

def is_int_in_st(2,a):
    current = a
    count = 1

    while current.next:
        current = current.next
        count += 1

    # calculate how far from the head to the kth
    distance_to_go = count - k

    current = a
    for i in range(distance_to_go):
        current = current.next

    return current

