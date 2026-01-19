class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (right + left) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:
                break
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        if mid == -1:
            mid = 0

        rotatedPoint = mid

        left = 0
        right = rotatedPoint
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = rotatedPoint + 1
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
