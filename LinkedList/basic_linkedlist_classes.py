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