class Solution:
    def jump(self, nums: List[int]) -> int:
        nextJumpRangeLeftPointer = 0
        nextJumpRangeRightPointer = 0
        counter = 0
        while nextJumpRangeRightPointer < len(nums) - 1:
            counter = counter + 1
            newNextJumpRangeRightPointer = 0
            while nextJumpRangeLeftPointer <= nextJumpRangeRightPointer:
                temp = nextJumpRangeLeftPointer + nums[nextJumpRangeLeftPointer]
                if newNextJumpRangeRightPointer < temp:
                    newNextJumpRangeRightPointer = temp
                nextJumpRangeLeftPointer = nextJumpRangeLeftPointer + 1
            nextJumpRangeRightPointer = newNextJumpRangeRightPointer

        return counter
