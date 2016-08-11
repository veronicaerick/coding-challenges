class Node(object):
	""" Singly linked list node representation """

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __repr__(self):
		return "Node(%s)" % str(self.data)


class LinkedList(object):
	""" Singly linked list implementation """

	def __init__(self, head=None):
		self.head = head

def reverse_ll(lst):
    current = head
    previous = None

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    lst.head = previous

def search(self, data):
    current = self.head
    while current is not None:
        if current.data == data:
            return current

def size(self):
    current = self.head
    count = 0

    while current is not None:
        count += 1
        current = current.next

    return count
