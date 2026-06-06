class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tempCounter = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= tempCounter:
                tempCounter = 1
            else:
                tempCounter = tempCounter + 1

        return tempCounter == 1
