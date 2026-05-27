class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answers = [[]]
        nums.sort()
        new_size = 0

        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start = new_size
            new_size = len(answers)
            for j in range(start, new_size):
                answers.append(answers[j] + [nums[i]])
        return answers
