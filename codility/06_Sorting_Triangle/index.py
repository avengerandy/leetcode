# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = list(filter(lambda x: x > 0, A))

    totalSize = len(A)
    if (totalSize < 3):
        return 0

    A.sort()
    for index in range(totalSize - 2):
        if (
            (A[index] + A[index + 1] > A[index + 2]) and
            (A[index + 1] + A[index + 2] > A[index]) and
            (A[index + 2] + A[index] > A[index + 1])
        ):
            return 1
    return 0
