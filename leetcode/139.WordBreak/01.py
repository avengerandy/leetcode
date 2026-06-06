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

    def searchEnd(self, word: str, index: int) -> List[int]:
        node = self.root
        end = []
        for i in range(index, len(word)):
            char = word[i]
            if node.children.get(char):
                node = node.children[char]
                if node.isEnd:
                    end.append(i)
            else:
                return end
        return end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = PrefixTree()
        for word in wordDict:
            trie.insert(word)

        canBreak = [False] * (len(s) + 1)
        canBreak[0] = True
        for i in range(0, len(s) + 1):
            if not canBreak[i]:
                continue

            indexs = trie.searchEnd(s, i)
            for index in indexs:
                canBreak[index + 1] = True

        return canBreak[-1]
