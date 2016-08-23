# first, find right most element since its the largest using a recursive approach

def largest_BST(node):
    if node.right:
        largest_BST(node.right)

    return node.value 

def second_largest_BST(node):
    if node is None:
        return None

    if node.left and node.right:
        return(largest(node.left))
    # were at parent of largest, and there is no left subtree so largest
    # is current node
    if node.right and not node.right.left and not node.right.right:
        return node.value

    # if not, step right
    return(second_largest_BST(node.right))