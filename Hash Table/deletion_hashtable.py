"""Deletion in a Hash Table"""


class HashEntry:
    def __init__(self, key, data):
        self.key = key
        self.value = data
        self.nxt = None


class HashTable:
    def __init__(self):
        self.slots = 10
        self.size = 0
        self.bucket = [None] * self.slots
        self.threshold = 0.6

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def get_index(self, key):
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * self.slots

        for i in range(0, len(self.bucket)):
            head = self.bucket[i]

            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            node = None
                        elif node.next is None:
                            node.next = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.next
                head = head.next

        self.bucket = new_bucket
        self.slots = new_slots

    def insert(self, key, value):
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            self.size += 1
        else:
            head = self.bucket[b_index]
            while head is not None:
                if head.key is key:
                    head.value = value
                    break
                elif head.nxt is None:
                    head.nxt = HashEntry(key, value)
                    self.size += 1
                    break
                else:
                    head = head.nxt

        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()

    def search(self, key):
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.nxt
        return None

    def delete(self, key):
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        if head.key is key:
            self.bucket[b_index] = head.nxt
            self.size -= 1
            return self
        prev = None
        while head is not None:
            if head.key is key:
                prev.nxt = head.nxt
                self.size -= 1
                return
            prev = head
            head = head.nxt

        print("key not found")
        return


# Complete implementation of Hash Table
# set and dict in Python works like this
ht = HashTable()
ht.insert(2, "London")
ht.insert(7, "Paris")
ht.insert(22, "India")
ht.insert(8, "Cairo")
print(f"Size: {ht.get_size()}")
ht.delete(2)
print(f"New Size: {ht.get_size()}")
print(ht.search(2))
print(ht.search(22))

table = HashTable()  # Create a HashTable
print(table.is_empty())
table.insert("This", 1)
table.insert("is", 2)
table.insert("a", 3)
table.insert("Test", 4)
table.insert("Driver", 5)
print("Table Size: " + str(table.get_size()))
print("The value for 'is' key: " + str(table.search("is")))
table.delete("is")
table.delete("a")
print("Table Size: " + str(table.get_size()))

# Search: Best = O(1); Worst = O(n)
# Insert: Best = O(1); Worst = O(n)
# Delete: Best = O(1); Worst = O(n)
