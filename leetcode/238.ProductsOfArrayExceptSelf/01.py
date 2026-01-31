class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cacheLeft = []
        cacheRight = [0] * len(nums)

        temp = 1
        for i in range(len(nums)):
            temp = temp * nums[i]
            cacheLeft.append(temp)

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            temp = temp * nums[i]
            cacheRight[i] = temp

        ans = []
        for i in range(len(nums)):
            cacheLeftNumber = 1
            cacheRightNumber = 1
            if i > 0:
                cacheLeftNumber = cacheLeft[i - 1]
            if i < len(nums) - 1:
                cacheRightNumber = cacheRight[i + 1]
            ans.append(cacheLeftNumber * cacheRightNumber)

        return ans
