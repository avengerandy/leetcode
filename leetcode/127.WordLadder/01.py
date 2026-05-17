from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        L = len(beginWord)
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, level = queue.popleft()

            for i in range(L):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                for neighbor in neighbors[pattern]:
                    if neighbor == endWord:
                        return level + 1

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                neighbors[pattern] = []

        return 0
