class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1

        while numbers[pointer1] + numbers[pointer2] != target:
            if numbers[pointer2] >= target:
                pointer2 = pointer2 - 1
                continue
            if numbers[pointer1] + numbers[pointer2] > target:
                pointer2 = pointer2 - 1
                continue
            pointer1 = pointer1 + 1

        if pointer1 > pointer2:
            return [pointer2 + 1, pointer1 + 1]

        return [pointer1 + 1, pointer2 + 1]
