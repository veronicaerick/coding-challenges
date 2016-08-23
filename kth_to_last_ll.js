function kthToLast(head, k) {
    // start at head
    var left = head
    var right = head
    // move through ll, while n is smaller than k
    for (var n=0; n < k; n++) {
        right = right.next
    }
    // while we are not at the end of the list,
    // iterate through with both pointers until we
    // are at the end, so the left pointer will be at
    // k
    while (right.next) {
        left = left.next
        right = right.next
    }

    return left
}