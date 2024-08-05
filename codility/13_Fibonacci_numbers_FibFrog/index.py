# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.append(1)
    totalSize = len(A)
    fibonacci = [1, 2]
    for index in range(2, totalSize):
        nextFibonacci = fibonacci[index - 1] + fibonacci[index - 2]
        fibonacci.append(nextFibonacci)
        if (nextFibonacci > totalSize):
            break

    dp = {-1:0}
    for index in range(totalSize):
        if (A[index] == 0):
            continue
        temp = []
        for number in fibonacci:
            if number > index + 1:
                break
            if index - number in dp:
                temp.append(dp[index - number] + 1)
        if (temp):
            dp[index] = min(temp)
    return dp.get(totalSize - 1, -1)
