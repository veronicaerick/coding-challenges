def have_cycles(head):
    slow = head
    fast = head 

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next

        if fast == slow:
            return True

    return False

def reverse_inplace(head):
    current = head
    previous = None

    while current != None:
        # copy a pointer to next
        next = current.next
        # reverse pointer
        current.next = previous
        # steo forward
        previous = current
        
        current = next
    # previous—was the tail of the original list, and thus the head of our reversed list
    return previous

def kth_to_lastnode(k, head):
    # kth_to_lst(2, head):
    # get the length, minus k from that, and stop at that point
    if k < 1:
        raise valueError

    list_len = 1
    current = head

    while current is not None:
        current = current.next
        list_len += 1

    if k > len(list_len):
        raise valueError

    # walk through the list and stop at k
    place to stop = list_len - k
    current = head
    for i in range(len(place_to_stop)):
        current = current.next

    return current

