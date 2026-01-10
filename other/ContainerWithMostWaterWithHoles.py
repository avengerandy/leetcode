# Container With Most Water With Holes
#
# Given an array of heights, some positions are "holes" that cannot store water.
# A container may span across holes, but water leaks at hole positions.
# Return the maximum possible container area.
#
# Tips:
# Holes split containers into multiple independent subcontainers.
# The maximum area of a container spanning multiple holes is the sum of the areas
# of its subcontainers.
#
# Example:
# height = [1,8,6,2,5,4,8,3,7]
# holes = {3, 6}
# container = [1,8,6] | hole | [5,4] | hole | [3,7]

from typing import List, Set

class Solution:
    def maxAreaWithHoles(self, height: List[int], holes: Set[int]) -> int:
        n = len(height)
        max_area = 0

        # Step 1: Generate hole-free segments. O(n)
        segments = []
        start = 0
        for i in range(n):
            if i in holes:
                if start < i:
                    segments.append((start, i - 1))
                start = i + 1
        if start < n:
            segments.append((start, n - 1))

        # Step 2: Precompute four-case max for each segment. O(n)
        segment_max = {}
        for l, r in segments:
            # full: both ends fixed
            full = (r - l) * min(height[l], height[r])
            # left fixed
            left = self._one_side_pointer_max(height, l, r, left_fixed=True)
            # right fixed
            right = self._one_side_pointer_max(height, l, r, left_fixed=False)
            # both flexible
            both = self._two_pointer_max(height, l, r)
            segment_max[(l, r)] = {
                'full': full,
                'left': left,
                'right': right,
                'both': both
            }

        # Step 3: Iterate all segments pairs. [n * (n + 1)]/2 = O(n²)
        max_area = 0
        n_seg = len(segments)

        for length in range(1, n_seg + 1):
            for start in range(n_seg - length + 1):
                sub_area = 0
                if length == 1:
                    sub_area = segment_max[segments[start]]['both']
                else:
                    for idx in range(start, start + length):
                        l, r = segments[idx]
                        if idx == start:
                            sub_area += segment_max[(l, r)]['right']
                        elif idx == start + length - 1:
                            sub_area += segment_max[(l, r)]['left']
                        else:
                            sub_area += segment_max[(l, r)]['full']
                max_area = max(max_area, sub_area)

        return max_area

    def _two_pointer_max(self, height: List[int], l: int, r: int) -> int:
        i, j = l, r
        max_area = 0
        while i < j:
            h = min(height[i], height[j])
            w = j - i
            max_area = max(max_area, h * w)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

    def _one_side_pointer_max(self, height: List[int], l: int, r: int, left_fixed: bool) -> int:
        if left_fixed:
            fixed_height = height[l]
            max_area = 0
            for j in range(l + 1, r + 1):
                area = (j - l) * min(fixed_height, height[j])
                max_area = max(max_area, area)
            return max_area
        else:
            fixed_height = height[r]
            max_area = 0
            for i in range(l, r):
                area = (r - i) * min(height[i], fixed_height)
                max_area = max(max_area, area)
            return max_area


if __name__ == "__main__":
    sol = Solution()

    height = [1,8,6,2,5,4,8,3,7]
    holes = {3, 6}

    max_area = sol.maxAreaWithHoles(height, holes)
    print("Max area with holes:", max_area) #13

    height = [14,14,6,2,5,4,8,3,7]
    holes = {3, 6}

    max_area = sol.maxAreaWithHoles(height, holes)
    print("Max area with holes:", max_area) #19

    height = [14,14,1,2,5,4,8,3,7]
    holes = {3, 6}

    max_area = sol.maxAreaWithHoles(height, holes)
    print("Max area with holes:", max_area) #14
