class Node:
    def __init__(self, name=""):
        self.name = name # for test
        self.transitions = {}  # 'a'
        self.epsilon_transitions = []  # '*'
        self.isEnd = False

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # pattern to NFA with end node
        nodes = [Node(f"P{i}") for i in range(len(p) + 1)]

        i = 0
        while i < len(p):
            char = p[i]
            if i + 1 < len(p) and p[i + 1] == '*':
                # 1. zero time jump
                nodes[i].epsilon_transitions.append(nodes[i + 2])

                # 2. one or more time loops
                if char not in nodes[i].transitions:
                    nodes[i].transitions[char] = []
                nodes[i].transitions[char].append(nodes[i])
                i += 2
            else:
                if char not in nodes[i].transitions:
                    nodes[i].transitions[char] = []
                nodes[i].transitions[char].append(nodes[i + 1])
                i += 1
        nodes[-1].isEnd = True

        # DFS
        memo = {}
        def can_reach_end(curr_node_idx, s_idx):
            state = (curr_node_idx, s_idx)
            if state in memo: return memo[state]

            curr_node = nodes[curr_node_idx]

            # end
            if s_idx == len(s):
                if curr_node.isEnd:
                    return True
                for next_node in curr_node.epsilon_transitions:
                    if can_reach_end(nodes.index(next_node), s_idx):
                        return True
                return False

            # go by 1. zero time jump
            for next_node in curr_node.epsilon_transitions:
                if can_reach_end(nodes.index(next_node), s_idx):
                    memo[state] = True
                    return True

            # go by 2. one or more time loops
            char_to_match = s[s_idx]
            for move_char, next_nodes in curr_node.transitions.items():
                if move_char == char_to_match or move_char == '.':
                    for n in next_nodes:
                        if can_reach_end(nodes.index(n), s_idx + 1):
                            memo[state] = True
                            return True

            memo[state] = False
            return False

        return can_reach_end(0, 0)
