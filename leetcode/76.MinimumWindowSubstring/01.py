from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        target_counts = Counter(t)
        window_counts = {}

        satisfied = 0
        required = len(target_counts)

        ans = (float('inf'), None, None)
        left = 0
        for right, char in enumerate(s):
            if char in target_counts:
                window_counts[char] = window_counts.get(char, 0) + 1
                if window_counts[char] == target_counts[char]:
                    satisfied += 1

            while satisfied == required:
                current_window_len = right - left + 1
                if current_window_len < ans[0]:
                    ans = (current_window_len, left, right)
                left_char = s[left]

                if left_char in target_counts:
                    window_counts[left_char] -= 1
                    if window_counts[left_char] < target_counts[left_char]:
                        satisfied -= 1
                left += 1

        return '' if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]
