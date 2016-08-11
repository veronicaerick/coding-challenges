def middle_ll(self):
    current = self.head
    slow = current
    fast = current

    while current is not None:
        slow = current.next
        fast = current.next.next
        if fast = None:
            return slow.data
