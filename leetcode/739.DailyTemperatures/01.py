class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stask = []
        temp = 0
        for i in range(len(temperatures)):
            temp = 0
            while len(stask) and stask[-1][1] < temperatures[i]:
                temp = temp + 1
                idx, _ = stask.pop()
                res[idx] = i - idx
            stask.append((i, temperatures[i]))
        return res
