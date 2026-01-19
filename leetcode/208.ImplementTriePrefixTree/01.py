class Node:
   def __init__(self):
        self.children = dict()
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.children.get(char):
                node = node.children[char]
            else:
                node.children[char] = Node()
                node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.children.get(char):
                node = node.children[char]
            else:
                return False
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node.children.get(char):
                node = node.children[char]
            else:
                return False
        return True
