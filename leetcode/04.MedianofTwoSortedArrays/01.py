class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0:
            if not (len(nums2) % 2):
                return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2
            else:
                return nums2[len(nums2) // 2]

        total = len(nums1) + len(nums2)
        if not (total % 2):
            pointMedian = total // 2 - 1
        else:
            pointMedian = total // 2

        point1 = 0
        point2 = 0
        tempCounter = 0
        while tempCounter < pointMedian:
            if point1 + 1 == len(nums1):
                point2 = point2 + 1
            elif point2 + 1 == len(nums2):
                point1 = point1 + 1
            elif nums1[point1 + 1] < nums2[point2 + 1]:
                point1 = point1 + 1
            else:
                point2 = point2 + 1
            tempCounter = tempCounter + 1

        median = nums1[point1] if nums1[point1] < nums2[point2] else nums2[point2]
        if total % 2:
            return median

        if point1 > 0 and point1 + 1 <= len(nums1) and nums1[point1] < nums2[point2]:
            if nums1[point1 - 1] < nums2[point2]:
                return (median + nums2[point2]) / 2
            else:
                return (median + nums1[point1 - 1]) / 2
        else:
            if nums2[point2] - 1 < nums1[point1]:
                return (median + nums1[point1]) / 2
            else:
                return (median + nums2[point2 - 1]) / 2
