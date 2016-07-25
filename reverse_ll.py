def reverse_ll(lst):
    previous = None
    current = head

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return lst.head = previous
