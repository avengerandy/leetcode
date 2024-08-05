# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    return int(N / gcd(N, M))

def gcd(N, M):
    mod = N % M
    if (mod == 0):
        return M
    return gcd(M, mod)
