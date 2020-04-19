# Merge two sorted linked list

# Create Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# Create linked list class
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

		if self.head is None:
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
			print("Previous node does not exist.")
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

		if not cur_node:
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
			count = 1

			while cur_node and count != pos:
				prev = cur_node
				cur_node = cur_node.next
				count += 1

			if not cur_node:
				return

			prev.next = cur_node.next
			cur_node = None


	def len_iterative(self):

		cur_node = self.head
		count = 0

		while cur_node:
			count += 1
			cur_node = cur_node.next

		return count

	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)


	def swap_nodes(self, key_1, key_2):

		if key_1 == key_2:
			return

		prev_1 = None
		curr_1 = self.head

		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next

		if not curr_1:
			return

		prev_2 = None
		curr_2 = self.head

		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2
			curr_2 = curr_2.next

		if not curr_2:
			return

		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2

		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1

		curr_1.next, curr_2.next = curr_2.next, curr_1.next

	def print_helper(self, node, name):
		if node is None:
			print(name + ": None")

		else:
			print(name + ":" + node.data)


	def reverse_iterative(self):
		prev = None
		cur = self.head

		while cur:
			nxt = cur.next
			cur.next = prev

			self.print_helper(prev, "PREV")
			self.print_helper(cur, "CUR")
			self.print_helper(nxt, "NXT")
			print("\n")

			prev = cur
			cur = nxt

		self.head = prev


	def reverse_recursive(self):

		def _reverse_recursive(cur, prev):
			if not cur:
				return prev

			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			return _reverse_recursive(cur, prev)

		self.head = _reverse_recursive(cur=self.head, prev=None)


	# Merge two sorted linked lists
	def merge_sorted(self, llist):

		p = self.head
		q = llist.head
		s = None

		if not p:
			return q
		if not q:
			return p

		if p and q:
			if p.data <= q.data:
				s = p
				p = s.next

			else:
				s = q
				q = s.next

			new_head = s

		while p and q:
			if p.data <= q.data:
				s.next = p
				s = p
				p = s.next

			else:
				s.next = q
				s = q
				q = s.next

		if not p:
			s.next = q
		if not q:
			s.next = p

		return new_head


llist = LinkedList()

print(f"The length of an empty linked list is --> {(llist.len_recursive(llist.head))}")

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.prepend("pre-A")

llist.insert_after_node(llist.head.next, "post-A")

llist.print_list()

print("Reversing the list iteratively......")
llist.reverse_iterative()
llist.print_list()


print("Original List")
llist.print_list()


llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same")
llist.print_list()

print("Reversing the list recursively........")
llist.reverse_recursive()

llist.print_list()


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


llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

print("----------Linked List - 1-------------")
llist_1.print_list()

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

print("----------Linked List - 2-------------")
llist_2.print_list()



llist_1.merge_sorted(llist_2)
print("----------Merged Linked List-------------")
llist_1.print_list()

print(f"The length of a linked list calculated iteratively after removing 3 elements is --> {(llist.len_iterative())}")