class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = set()

        for triplet in triplets:
            if triplet[0] > target[0]:
                continue
            if triplet[1] > target[1]:
                continue
            if triplet[2] > target[2]:
                continue
            for idx, value in enumerate(triplet):
                if value == target[idx]:
                    match.add(idx)
        return len(match) == 3
