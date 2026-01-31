"""
BINARY SEARCH BOUNDARY STRATEGY:
-----------------------------------------------------------------------
1. SEARCHING FOR A SPECIFIC VALUE (Find target and return immediately)
   - Condition: while left <= right
   - Update:    left = mid + 1 / right = mid - 1
   - Why:       Since we check nums[mid] == target, we can safely exclude mid.

2. SEARCHING FOR A BOUNDARY/LIMIT (Find the first/last element meeting a condition)
   - Condition: while left < right
   - Update:
        - If mid could be the answer: keep it (e.g., right = mid)
        - If mid is definitely NOT the answer: exclude it (e.g., left = mid + 1)
   - Result:    Exits when left == right, pointing at the critical boundary.

3. PREVENTING INFINITE LOOPS:
   - If using 'left = mid', calculate mid as: mid = (left + right + 1) // 2 (Round Up)
   - If using 'right = mid', calculate mid as: mid = (left + right) // 2     (Round Down)
-----------------------------------------------------------------------
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0

        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]: # right side Rotated
                left = mid + 1
            else:
                right = mid

        return nums[right]
