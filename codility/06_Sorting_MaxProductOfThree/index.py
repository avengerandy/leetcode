# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    first = A[-1] * A[-2] * A[-3]
    second = A[-1] * A[0] * A[1]
    return max(first, second)
