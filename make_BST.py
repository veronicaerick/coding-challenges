def make_BST(nums):
    # base_case
    if not nums:
        return None

    # find the mid point in list
    middle = len(nums)/2

    # make node in the middle 
    node = BinaryNone(nums[middle])

    # recursively find left and right nodes
    node.left = make_BST(nums[:middle])
    node.right = make_BST(nums[middle + 1:])

    return node
