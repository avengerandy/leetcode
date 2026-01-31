class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        leftHasZero = False
        topHasZero = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                leftHasZero = True
                break

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                topHasZero = True
                break

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if leftHasZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if topHasZero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
