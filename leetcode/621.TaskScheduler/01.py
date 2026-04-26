class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        f_max = max(counts.values())

        k = sum(1 for count in counts.values() if count == f_max)
        res = (f_max - 1) * (n + 1) + k

        return max(len(tasks), res)
