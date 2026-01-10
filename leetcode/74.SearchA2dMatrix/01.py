class Solution:
    matrix = None
    rowSize = 0

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.matrix = matrix
        self.rowSize = len(matrix[0])

        left = 1
        right = len(matrix) * self.rowSize

        while True:
            center = ((right - left) // 2) + left
            if self.getValue(center) == target or self.getValue(right) == target:
                return True
            if center == left:
                return False

            if self.getValue(center) > target:
                right = center
            else:
                left = center

    def getValue(self, index: int):
        index = index - 1
        colLocation = index // self.rowSize
        rowLocation = index % self.rowSize
        return self.matrix[colLocation][rowLocation]
