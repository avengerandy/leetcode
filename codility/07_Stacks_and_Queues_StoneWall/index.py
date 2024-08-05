# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    total = 0
    stack = []
    for high in H:

        while(len(stack) > 0):
            prevHigh = stack[-1]

            if (high == prevHigh):
                break

            if (high > prevHigh):
                total = total + 1
                stack.append(high)
                break

            stack.pop()

        if (len(stack) == 0):
            total = total + 1
            stack.append(high)

    return total
