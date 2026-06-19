class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        curr = 0
        for g in gain:
            curr += g
            m = max(curr, m)
        return m
