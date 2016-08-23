def reverse_ll(head):
    n = head
    new_head = None

    while n is not None:
        new_head = Node(n.data, new_head)
        n = n.next

def reverse_ll_inplace(lst):
    current = lst.head
    previous = None

    while current != None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return lst.head = previous


