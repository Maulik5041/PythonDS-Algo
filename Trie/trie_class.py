"""Implementation of a typical trie class"""


class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.children = [None] * 26
        self.is_end_word = False

    def mark_as_leaf(self):
        self.is_end_word = True

    def unmark_as_leaf(self):
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        return ord(t) - ord('a')

    def insert(self, key):
        if not key:
            return

        key = key.lower()
        current_node = self.root
        index = 0

        for level, _ in enumerate(key):
            index = self.get_index(key[level])

            if not current_node.children[index]:
                current_node.children[index] = TrieNode(key[level])
                print(key[level] + " inserted")

            current_node = current_node.children[index]

        current_node = current_node.mark_as_leaf()
        print("'" + key + "' inserted")

    def search(self, key):
        if not key:
            return False

        key = key.lower()
        current_node = self.root
        index = 0

        for level, _ in enumerate(key):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]

        if current_node and current_node.is_end_word:
            return True

        return False

    def delete(self, key):
        # Function to delete a given key from Trie
        if not self.root or not key:
            print("None key or empty trie error")
            return
        self.delete_helper(key, self.root, len(key), 0)

    def delete_helper(self, key, current_node, length, level):
        deleted_self = False

        if not current_node:
            print("key does not exist")
            return deleted_self

        # Base case:
        # If we have reached at the node
        # which points to the alphabet at the end of the key
        if level == length:
            # If there are no nodes ahead of this node in this
            # path, then we can delete this node
            if self.has_no_children(current_node):
                current_node = None
                deleted_self = True

            # If there are nodes ahead of current_node in this path
            # Then we cannot delete current_node
            # We simply unmark this as leaf
            else:
                current_node.unmark_as_leaf()
                deleted_self = False

        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(key, child_node, length, level+1)

            if child_deleted:
                # Making children pointer also None: since child is deleted
                current_node.children[self.get_index(key[level])] = None

                # If current_node is leaf node then
                # current_node is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current_node.is_end_word:
                    deleted_self = False

                # If child_node is deleted and current_node has more children
                # then current_node must be part of another key
                # So, we cannot delete current_node
                elif self.has_no_children(current_node) is False:
                    deleted_self = False

                # else we can delete current_node
                else:
                    current_node = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    def has_no_children(self, current_node):
        for i, _ in enumerate(current_node.children):
            if current_node.children[i]:
                return False

        return True


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
output = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: ")
print(keys)

for i, _ in enumerate(keys):
    t.insert(keys[i])

# Search for diferent keys
if t.search("the"):
    print("the --- " + output[1])
else:
    print("the --- " + output[0])

if t.search("these"):
    print("these --- " + output[1])
else:
    print("these --- " + output[0])

if t.search("abc"):
    print("abc --- " + output[1])
else:
    print("abc --- " + output[0])

t.delete("abc")
print("Deleted key \"abc\"")

if t.search("abc"):
    print("abc --- " + output[1])
else:
    print("abc --- " + output[0])
