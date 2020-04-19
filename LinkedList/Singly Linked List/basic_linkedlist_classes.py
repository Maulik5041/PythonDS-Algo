# Basic classes needed for all linked list implementation

# Creating a Node class with the data in it
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# Creating a linked list class that connects all the nodes created before
class LinkedList():

	def __init__(self):
		self.head = None

	# Printing the list
	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next