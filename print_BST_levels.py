def print_levels_BST(node):
    current_level = node

    while current_level:
        next_level = []
        for n in current_level:
            print n.data,
            if n.left:
               print next_level.append(n.left)
            if n.right:
                print next_level.append(n.right)

      
        current_level = next_level