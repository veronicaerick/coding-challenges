def depth(node):
    return max(depth(node.left), depth(node.right)) +1

def is_BST_balanced(node):
    if abs(depth(node.left) - depth(node.right)) >1:
        return False

    if is_BST_balanced(node.left) and is is_BST_balanced(node.right):
        return True