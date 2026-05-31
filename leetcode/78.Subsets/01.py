class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = [[]]
        for num in nums:
            for i in range(len(answers)):
                answers.append(answers[i] + [num])
        return answers
