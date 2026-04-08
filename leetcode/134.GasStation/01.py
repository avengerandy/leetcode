class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        ans = 0
        totalDiff = 0
        for i in range(len(gas)):
            totalDiff = totalDiff + gas[i] - cost[i]
            if totalDiff < 0:
                ans = i + 1
                totalDiff = 0

        return ans if i < len(gas) else -1
