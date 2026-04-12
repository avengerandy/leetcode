from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        hand.sort()
        for i in hand:
            if counter[i] > 0:
                for j in range(groupSize):
                    if counter[i + j] > 0:
                        counter[i + j] = counter[i + j] - 1
                    else:
                        return False
        return True
