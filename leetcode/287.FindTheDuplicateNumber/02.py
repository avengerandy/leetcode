class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # two step
            if slow == fast:
                break

        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast] # one step
            if slow == fast:
                return slow
