class Solution:
    SPLIT_SYMBOL = "ø"
    EMPTY_SYMBOL = "émpty"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.EMPTY_SYMBOL
        return self.SPLIT_SYMBOL.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.EMPTY_SYMBOL:
            return []
        return s.split(self.SPLIT_SYMBOL)
