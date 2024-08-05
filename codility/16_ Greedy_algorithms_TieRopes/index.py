# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    temp = 0
    total = 0
    for number in A:
        temp = temp + number
        if (temp >= K):
            temp = 0
            total = total + 1
    return total
