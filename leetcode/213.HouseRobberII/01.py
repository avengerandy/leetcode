class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax, prevPrevMax = 0, 0

        # not rob first
        for i in range(1, len(nums)):
            num = nums[i]
            ifRob = num + prevPrevMax
            ifNotRob = prevMax
            maxOfNum = max(ifRob, ifNotRob)
            prevPrevMax = prevMax
            prevMax = maxOfNum
        notRobFirst = prevMax

        # rob first
        prevMax, prevPrevMax = nums[0], 0
        maxOfNum = nums[0]
        for i in range(1, len(nums) - 1):
            num = nums[i]
            ifRob = num + prevPrevMax
            ifNotRob = prevMax
            maxOfNum = max(ifRob, ifNotRob)
            prevPrevMax = prevMax
            prevMax = maxOfNum
        robFirst = prevMax

        return max(robFirst, notRobFirst)
