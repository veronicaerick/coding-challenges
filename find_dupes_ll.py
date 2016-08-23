def remove_dupes(ll):
    current = ll.head
    previous = None
    dupe_set = set()

    while current != None:
        if current.data in dupe_set:
            if previous != None:
