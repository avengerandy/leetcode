# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(A, B):
    maxN = max(A)
    maxMod = math.pow(2, max(B))
    fibonacci = [1, 1]
    for index in range(2, maxN + 1):
        fibonacci.append((fibonacci[index - 1] + fibonacci[index - 2]) % maxMod)

    output = []
    for index in range(len(A)):
        ans = fibonacci[A[index]] % math.pow(2, B[index])
        output.append(int(ans))
    return output
