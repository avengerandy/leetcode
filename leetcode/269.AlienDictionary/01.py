class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        self.adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    self.adj[w1[j]].add(w2[j])
                    break

        self.visited = dict()
        self.ans = []
        for char in self.adj:
            if not self.dfs(char):
                return ""
        return "".join(self.ans[::-1])

    def dfs(self, char):
        if char in self.visited:
            return self.visited[char]

        self.visited[char] = False
        for neighbor in self.adj[char]:
            if not self.dfs(neighbor):
                return False

        self.visited[char] = True
        self.ans.append(char)
        return True
