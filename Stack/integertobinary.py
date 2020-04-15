# Using Stack to convert decimal to binary

class Stack():

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty:
			return self.items[-1]

	def get_stack(self):
		return self.items


def convert_int_to_bin(dec_num):
	s = Stack()

	while dec_num > 0:

		remainder = dec_num % 2
		s.push(remainder)
		dec_num //= 2

	bin_num = ""
	while not s.is_empty():
		bin_num += str(s.pop())


	return bin_num


print(convert_int_to_bin(10000))
print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))

print(int(convert_int_to_bin(56), 2)==56)
