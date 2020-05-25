"""Sort the list using Trie"""


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

    def get_root(self):
        return self.root

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
            current_node = current_node.children[index]
        current_node.mark_as_leaf()

    def search(self, key):
        if not key:
            return False

        key = key.lower()
        current_node = self.root
        index = 0

        for level, _ in enumerate(key):
            index = self.get_index(key[level])

            if not current_node.children[index]:
                return False

            current_node = current_node.children[index]

        if current_node and current_node.is_end_word:
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
            if current_node.has_no_children(current_node):
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


def sort_list(arr):
    result = []

    trie = Trie()
    for x, _ in enumerate(arr):
        trie.insert(arr[x])

    word = [''] * 20
    get_words(trie.get_root(), result, 0, word)
    return result


def get_words(root, result, level, word):
    if root.is_end_word:
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(temp)

    for i in range(26):
        if root.children[i]:
            word[level] = chr(i + ord('a'))
            get_words(root.children[i], result, level + 1, word)


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
print(sort_list(keys))
