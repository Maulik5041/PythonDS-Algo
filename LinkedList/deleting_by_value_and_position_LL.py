# Deleting a node on the basis of its value and position in a linked list

# Creating Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# Creating Linked List class
class LinkedList():

	def __init__(self):
		self.head = None

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next


	def append(self, data):
		new_node = Node(data)

		if not self.head:
			self.head = new_node
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next

		last_node.next = new_node


	def prepend(self, data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node


	def insert_after_node(self, prev_node, data):
		new_node = Node(data)

		if not prev_node:
			print("Previous node does not exist")
			return

		new_node.next = prev_node.next
		prev_node.next = new_node


	# Deleting a Node by it's value (data of the node)
	def delete_node(self, key):

		# Deleting the HEAD node
		cur_node = self.head

		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None
			return


		# Deleting a node which is NOT the head
		prev = None
		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next

		if cur_node is None:
			return

		prev.next = cur_node.next
		cur_node = None


	# Deleting a node at a given position
	def delete_node_at_pos(self, pos):
		if self.head:
			cur_node = self.head
			if pos == 0:
				self.head = cur_node.next
				cur_node = None
				return

			prev = None
			count = 0
			while cur_node and count != pos:
				prev = cur_node
				cur_node = cur_node.next
				count += 1

			if cur_node is None:
				return

			prev.next = cur_node.next
			cur_node = None



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.prepend("pre-A")

llist.insert_after_node(llist.head.next, "post-A")

print("------Before Deleting by value--------")
llist.print_list()

llist.delete_node("pre-A")
llist.delete_node("D")

print("------After Deleting by value ::pre-A:: and ::D::--------")
llist.print_list()


print("------After Deleting at position 2--------")
llist.delete_node_at_pos(2)
llist.print_list()