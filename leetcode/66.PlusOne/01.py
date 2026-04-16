class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 0
        digits[-1] = digits[-1] + 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + temp
            if digits[i] > 9:
                digits[i] = digits[i] % 10
                temp = 1
            else:
                temp = 0
                break

        if temp:
            return [1] + digits
        return digits
