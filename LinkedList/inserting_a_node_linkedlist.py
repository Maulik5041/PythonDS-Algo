# Inserting a node at various positions in a linked list

# Creating a Node Class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# Creating a Linked List class
class LinkedList():

	def __init__(self):
		self.head = None

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next

	# Inserting a node at the end (append) of an Empty and Non-Empty Linked List
	def append(self, data):
		new_node = Node(data)

		# Empty Linked List
		if self.head is None:
			self.head = new_node
			return

		# Non-Empty Linked List
		last_node = self.head
		while last_node.next:
			last_node = last_node.next

		last_node.next = new_node


	# Inserting a node at the beginning (prepend) of a Linked List
	def prepend(self, data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node

	# Inserting a Node after a specific Node (key)
	def insert_after_node(self, prev_node, data):
		if not prev_node:
			print("Previous node does not exist")
			return

		new_node = Node(data)

		new_node.next = prev_node.next
		prev_node.next = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.prepend("pre-A")

llist.insert_after_node(llist.head.next, "post-A")

llist.print_list()