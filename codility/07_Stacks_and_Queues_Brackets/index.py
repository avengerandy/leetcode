# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    totalSize = len(S)
    stack = []
    for character in S:
        if character in ['(', '[', '{']:
            stack.append(character)
            if (len(stack) > totalSize / 2):
                return 0
        else:
            if (len(stack) == 0):
                return 0
            popCharacter = stack.pop()
            if (character == ')' and popCharacter != '('):
                return 0
            if (character == ']' and popCharacter != '['):
                return 0
            if (character == '}' and popCharacter != '{'):
                return 0
    if (len(stack) != 0):
        return 0
    return 1
