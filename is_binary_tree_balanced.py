# calculate depth, then see if the depth of any two levels
# is more than one

def depth(node):
    return max(depth(node.left), depth(node.right))

def is_BT_balanced(node):
    if abs(depth(node.left) -depth(node.right)) > 1:
        return False

    if is_BT_balanced(node.left) and is is_BT_balanced(node.right):
        return True
# ##################### V2 ############################

def is_balanced(root):
    depths = []

    nodes = []
    nodes.append((root,0))
    # get a node from the top of the stack
    while len(nodes):
        node, depth = nodes.pop()

        # in case its a leaf
        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)

                if (len(depths) > 2) or \
                    (len(depths) == 2) and abs(depths[0] - depths[1]> 1):
                    return False

        else:
            if node.left:
                nodes.append(node.left, depth + 1)
            if node.right:
                nodes.append(node.right, depth + 1)

    return True


