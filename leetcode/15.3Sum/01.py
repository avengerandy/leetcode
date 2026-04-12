class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            num = nums[idx]
            res_list = self.twoSumAll(nums[idx+1:], -num)

            for res in res_list:
                res.append(nums[idx])
                ans.append(res)
        return ans

    def twoSumAll(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        cache = set()
        seen_pairs = set()

        for num in nums:
            diff = target - num
            if diff in cache:
                pair = tuple(sorted([diff, num]))
                if pair not in seen_pairs:
                    results.append([diff, num])
                    seen_pairs.add(pair)
            cache.add(num)

        return results
