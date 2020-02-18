from collections import defaultdict


class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = defaultdict()
        self.counter = 1
        self.isEndOfWord = False
        self.links = []



class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        return TrieNode()

    def _charToIndex(self, ch):

        return ord(ch) - ord('a')

    def insert(self, key,link):

        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if index not in node.children:
                node.children[index] = self.getNode()
            node = node.children[index]

            # mark last node as leaf

        node.isEndOfWord = True

        node.links.append(link)
    def search(self, key):
        node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if index not in node.children:
                return False
            node =  node.children[index]
        if node != None and  node.isEndOfWord:
            return True
        else:
            return False


