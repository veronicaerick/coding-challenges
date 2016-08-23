def print_BT(node):
    current_level = node
    # create list for next level, look at each node in current and
    # print the data. If there are children of this node on the left
    # or right, add those to next level and when were done, move from current
    # to next level
    while current_level != None:
        next_level = []
        for nodes in current_level:
            print node.data,
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)

        print 
        current_level = next_level


def depth(node):
    if not node:
        return

    return max(depth(node.left), depth(node.right)) + 1

def is_balanced(node):
    if not node:
        return True

    if abs(depth(node.left)- depth(node.right)) > 1:
        return False

    if is_balanced(node.right) and is_balanced(node.left):
        return True

def is_BST(node):
    previos = None
    if node is None:
        return None
    # if there is no left, its not a BST
    if not is_BST(node.left):
        return False
    # if we arent at the root and our data is smaller than the last
    # node we saw, return false
    if previous != None and node.data <= previous:
        return False
    # move through tree
    previous = node.data

    if not is_BST(node.right):
        return False

    return True

# in order traversal with a stack
def kth_smallest_BST(root, k):
    will_visit = []
    current = root

    while current != None:
        will_visit.append(node)
        current = current.left

    count = 0

    while will_visit and count < k:
        current = will_visit.pop()
        count += 1
        right = current.right
        while right: 
            stack.append(right)
            right = right.left

    return current.data


