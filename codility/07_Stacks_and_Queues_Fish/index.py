# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    totalSize = len(A)
    stack = []
    for index in range(totalSize):
        if (B[index] == 1):
            stack.append(A[index])
        else:
            while (len(stack) > 0):
                upFishSize = A[index]
                downFishSize = stack.pop()
                totalSize = totalSize - 1
                if (upFishSize < downFishSize):
                    stack.append(downFishSize)
                    break
    return totalSize
