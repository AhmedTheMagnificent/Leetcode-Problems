class Solution:
    def maxOperations(self, s: str) -> int:
        sm = ""
        for c in s:
            if sm and sm[-1] == "0" and c == "0":
                continue
            sm += c
        ones = 0
        ops = 0
        for c in sm:
            if c == "1":
                ones += 1
            else:
                ops += ones
        return ops