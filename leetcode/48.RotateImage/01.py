class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rowSize = len(matrix)
        step = 0
        while rowSize - (step * 2) > 1:
            end = rowSize - step - 1
            temp = 0
            for i in range(0, end - step):
                temp = matrix[step][step + i]
                matrix[step][step + i] = matrix[end - i][step]
                matrix[end - i][step] = matrix[end][end - i]
                matrix[end][end - i] = matrix[step + i][end]
                matrix[step + i][end] = temp
            step = step + 1
