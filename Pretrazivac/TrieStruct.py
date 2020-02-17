from typing import Tuple
class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False
        self.links = []

    def add(self, word,link):
        node = self
        word = word.lower()
        for char in word:
            found = False
            for child in node.children:
                if child.char == char:
                    found = True
                    node = child
                    break
            if not found:
                newNode = TrieNode(char)
                node.children.append(newNode)
                node = newNode
        node.word_finished = True
        node.links.append(link)

    def findWord(self, word):
        node = self
        word = word.lower()
        if not node.children:
            return False, 0
        for char in word:
            found = False
            for child in node.children:
                if child.char == char:
                    found = True
                    node = child
                    break
            if not found:
                return False, 0
        return True,




