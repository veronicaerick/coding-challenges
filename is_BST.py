def is_BST(node):
	if node is None:
		return True


	if not is_BST(node.left):
		return False

    previous = None

	if previous != None and node.data <= previous:
		return False

	previous = node.data

	if not is_BST(node.right):
		return False

	return True
