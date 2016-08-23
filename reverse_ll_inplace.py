def reverse_ll_inplace(head):
    current = head
    previous = None

    while current is != None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous