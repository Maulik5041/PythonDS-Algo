"""Total number of words in a Trie"""


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
                print(f"{(key[level])} inserted")

            current_node = current_node.children[index]

        current_node.mark_as_leaf()
        print(f"'{key}' inserted")

    def search(self, key):
        if not key:
            return False

        key = key.lower()
        current_node = self.root
        index = 0

        for level, _ in enumerate(key):
            index = self.get_index(key[index])

            if not current_node.children[index]:
                return False

            current_node = current_node.children[index]

        if current_node.is_end_word and current_node:
            return True

        return False

    def delete(self, key):
        if not key or not self.root:
            return

        self.delete_helper(key, self.root, len(key), 0)

    def delete_helper(self, key, current_node, length, level):
        deleted_self = False

        if not current_node:
            return deleted_self

        if length == level:
            if self.has_no_children(current_node):
                current_node = None
                deleted_self = True

            else:
                current_node.unmark_as_leaf()
                deleted_self = False

        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(key, child_node, length, level + 1)
            if child_deleted:
                current_node.children[self.get_index(key[level])] = None
                if current_node.is_end_word:
                    deleted_self = False

                elif not self.has_no_children(current_node):
                    deleted_self = False

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


def total_words(root):
    result = 0

    if root.is_end_word:
        result += 1

    for i in range(26):
        if root.children[i]:
            result += total_words(root.children[i])

    return result


trie = Trie()
keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

for key in keys:
    trie.insert(key)

print(total_words(trie.root))
