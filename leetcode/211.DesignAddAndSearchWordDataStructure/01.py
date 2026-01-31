class Node:
   def __init__(self):
        self.children = dict()
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.children.get(char):
                node = node.children[char]
            else:
                node.children[char] = Node()
                node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        return self.DFS(0, self.root, word)

    def DFS(self, index, node, word: str) -> bool:
        for i in range(index, len(word)):
            char = word[i]
            if char == ".":
                for child in node.children.values():
                    if self.DFS(i + 1, child, word):
                        return True
                return False
            else:
                if node.children.get(char):
                    node = node.children[char]
                else:
                    return False
        return node.isEnd
