# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def gcd(number1, number2):
    mod = number1 % number2
    if (mod == 0):
        return number2
    return gcd(number2, mod)

def sameSet(number, gcdAB):
    while (number != 1):
        temp = gcd(number, gcdAB)
        if (temp == 1):
            return False
        number = int(number / temp)
        if (number == 1):
            return True

def solution(A, B):
    counter = 0
    for index in range(len(A)):
        if (A[index] == B[index]):
            counter = counter + 1
            continue

        gcdAB = gcd(A[index], B[index])
        if (gcdAB == 1):
            continue

        if (sameSet(A[index], gcdAB) and sameSet(B[index], gcdAB)):
            counter = counter + 1
    return counter
