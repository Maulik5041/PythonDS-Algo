# Calculating the length of a linked list

# Creating a Node class
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

		if not prev_node:
			print("Previous node does not exist")
			return

		new_node = Node(data)

		new_node.next = prev_node.next
		prev_node.next = new_node


	def delete_node(self, key):
		cur_node = self.head

		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None
			return

		prev = None

		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next

		if cur_node is None:
			return

		prev.next = cur_node.next
		cur_node = None


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


			if not cur_node:
				return

			prev.next = cur_node.next
			cur_node = None


	# Calculating the length by iteration
	def len_iterative(self):

		count = 0
		cur_node = self.head
		while cur_node:
			count += 1
			cur_node = cur_node.next
		return count


	# Calculating the length by recursion
	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)


llist = LinkedList()

print(f"The length of an empty linked list is --> {(llist.len_recursive(llist.head))}")

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.prepend("pre-A")

llist.insert_after_node(llist.head.next, "post-A")

print(f"The length of a linked list calculated recursively after inserting 6 elements is --> {(llist.len_recursive(llist.head))}")

print("------Before Deleting by value--------")
llist.print_list()

llist.delete_node("pre-A")
llist.delete_node("D")

print("------After Deleting by value ::pre-A:: and ::D::--------")
llist.print_list()


print("------After Deleting at position 2--------")
llist.delete_node_at_pos(2)
llist.print_list()

print(f"The length of a linked list calculated iteratively after removing 3 elements is --> {(llist.len_iterative())}")