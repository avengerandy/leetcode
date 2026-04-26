class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        nums = list(map(int, s))

        dp1 = 0
        dp2 = 0
        for i in range(len(nums)):
            # cannot be decoded
            if nums[i] == 0 and i != 0 and nums[i - 1] not in [1, 2]:
                return 0

            tempAns = 0
            # single decoded
            if nums[i] >= 1 and nums[i] <= 9:
                if i == 0:
                    tempAns = 1
                    dp1 = dp2
                    dp2 = tempAns
                    continue
                tempAns = dp2

            # double decoded
            if nums[i - 1] == 1:
                if i == 1:
                    tempAns = tempAns + 1
                else:
                    tempAns = tempAns + dp1
            if nums[i - 1] == 2 and nums[i] <= 6:
                if i == 1:
                    tempAns = tempAns + 1
                else:
                    tempAns = tempAns + dp1

            dp1 = dp2
            dp2 = tempAns
        return dp2
