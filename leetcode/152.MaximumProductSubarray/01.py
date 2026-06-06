class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        postive = 1
        negtive = 1
        tempAns = 1
        ans = float('-inf')
        for num in nums:
            if num > 0:
                postive = postive * num
                negtive = negtive * num
                tempAns = postive
            if num < 0:
                tempAns = postive * num
                if negtive <= 0:
                    newPostive = negtive * num
                    negtive = postive * num
                    postive = newPostive
                    tempAns = newPostive
                else:
                    negtive = negtive * num
                    postive = 1
            if num == 0:
                postive = 1
                negtive = 1
                tempAns = 0
            ans = max(ans, tempAns)
        return ans
