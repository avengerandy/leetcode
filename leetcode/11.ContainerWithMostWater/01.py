class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointerLeft = 0
        pointerRight = len(heights) - 1
        maxWater = 0

        while pointerRight > pointerLeft:
            height = min(heights[pointerRight], heights[pointerLeft])
            width = pointerRight - pointerLeft
            water = height * width
            maxWater = max(maxWater, water)

            if heights[pointerRight] > heights[pointerLeft]:
                pointerLeft = pointerLeft + 1
            else:
                pointerRight = pointerRight - 1

        return maxWater
