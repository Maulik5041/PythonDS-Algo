"""Implementation of Hash Table"""


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

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    # Hash Function
    def get_index(self, key):
        hash_code = hash(key)
        index = hash_code % self.slots
        return index


ht = HashTable()
entry = HashEntry(3, "Educative")
print(f"{str(entry.key)}, {entry.value}")
print(ht.is_empty())
