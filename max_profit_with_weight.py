def ll_have_cycle(head):
    # both start at beggining
    fast_runner = current
    slow_runner = current
    while fast_runner != None and fast_runner.next != None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if fast_runner == slow_runner:
            return True

    return False
