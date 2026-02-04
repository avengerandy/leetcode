class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax, prevPrevMax = 0, 0

        for num in nums:
            ifRob = num + prevPrevMax
            ifNotRob = prevMax
            maxOfNum = max(ifRob, ifNotRob)
            prevPrevMax = prevMax
            prevMax = maxOfNum
        return prevMax
