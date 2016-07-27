def lowest_common_ancestor(root, n1, n2):
    if root is None:
        return None

    if n1 < root.data < n2:
        return root
    # if root is larger that n1 and n1, the LCA is on the left
    elif root.data > n1 and root.data > n2:
        return lowest_common_ancestor(root.left, n1, n2)

    else:
        return lowest_common_ancestor(root.right, n1, n2)
