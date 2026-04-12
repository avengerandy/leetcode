class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for idx in range(len(nums)):
            num = nums[idx]
            diff = target - num
            if diff in cache:
                return [cache[diff], idx]
            cache[num] = idx
        return []
