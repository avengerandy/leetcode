class Solution:
    def trap(self, height: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(height) - 1
        totalArea = 0
        rightHeight = 0
        leftHeight = 0

        while pointer1 < pointer2:
            if height[pointer1] > height[pointer2]:
                rightHeight = max(rightHeight, height[pointer2])
                water = rightHeight - height[pointer2]
                totalArea = totalArea + water
                pointer2 = pointer2 - 1
            else:
                leftHeight = max(leftHeight, height[pointer1])
                water = leftHeight - height[pointer1]
                totalArea = totalArea + water
                pointer1 = pointer1 + 1

        return totalArea
