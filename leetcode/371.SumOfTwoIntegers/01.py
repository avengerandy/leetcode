class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        add = (a ^ b) & mask
        carry = (a & b) << 1
        carry = carry & mask
        while carry & mask > 0:
            newAdd = (add ^ carry) & mask
            carry = (add & carry) << 1
            carry = carry & mask
            add = newAdd

        if add <= 0x7FFFFFFF:
            return add
        return ~(add ^ mask)
