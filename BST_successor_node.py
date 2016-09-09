# Given a node n in a binary search tree, explain and code the most efficient way to find the successor of n.
# Analyze the runtime complexity of your solution.

def find_inorder_ancestor(node):
    # Node n has a right child: in this case s is the node with the minimum key on n's right sub-tree.
    if node.right != None:
        # find minimum key within tree/ go furthest to the
        # left that we can 
        while node.left != None:
            node = node.left
        return node
    # look up to parent
    ancestor = node.parent
    # child is current node
    child = node
    # if current node has a parent node and current node is the right node
    while ancestor != None and child == ancestor.right:
        # move up a level
        child = ancestor
        # move up another level
        ancestor = child.parent
    return ancestor 