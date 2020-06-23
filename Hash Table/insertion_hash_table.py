"""Insertion in a Hash Table"""


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
            print(f"{key} - {value} inserted at index {b_index}")
            self.size += 1
        else:
            head = self.bucket[b_index]
            while head is not None:
                if head.key is key:
                    head.value = value
                    break

                elif head.nxt is None:
                    head.nxt = HashEntry(key, value)
                    print(f"{key} - {value} inserted at index {b_index}")
                    self.size += 1
                    break
                head = head.nxt

        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()


ht = HashTable()
ht.insert(2, "London")
ht.insert(12, "Moscow")
ht.insert(7, "Paris")

print(f"Size of the list: {str(ht.size)}")
