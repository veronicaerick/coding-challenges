def bst_checker(root):
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if (node.value < lower_bound) or (node.value > upper_bound):
            return False

        if node.right:
            # needs to be less than current node
            node_and_bounds_stack(node.left, lower_bound, node.value)

        if node.right:
            node_and_bounds_stack(node.right, node.value, upper_bound)


    return True