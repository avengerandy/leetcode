class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        left_limit = [0] * n
        right_limit = [0] * n

        left_limit[0] = -1
        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left_limit[p]
            left_limit[i] = p

        right_limit[n - 1] = n
        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = right_limit[p]
            right_limit[i] = p

        max_area = 0
        for i in range(n):
            width = right_limit[i] - left_limit[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area
