class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answers = [[]]
        for num in nums:
            new_answers = []
            for answer in answers:
                for i in range(len(answer) + 1):
                    temp = answer.copy()
                    temp.insert(i, num)
                    new_answers.append(temp)
            answers = new_answers
        return answers
