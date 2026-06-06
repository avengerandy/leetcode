class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        leftIndex = 0
        rightIndex = len(matrix[0])
        topIndex = 0
        bottomIndex = len(matrix)

        while leftIndex < rightIndex and topIndex < bottomIndex:
            for i in range(leftIndex, rightIndex):
                res.append(matrix[topIndex][i])
            topIndex += 1
            for i in range(topIndex, bottomIndex):
                res.append(matrix[i][rightIndex - 1])
            rightIndex -= 1
            if not (leftIndex < rightIndex and topIndex < bottomIndex):
                break
            for i in range(rightIndex - 1, leftIndex - 1, -1):
                res.append(matrix[bottomIndex - 1][i])
            bottomIndex -= 1
            for i in range(bottomIndex - 1, topIndex - 1, -1):
                res.append(matrix[i][leftIndex])
            leftIndex += 1

        return res
