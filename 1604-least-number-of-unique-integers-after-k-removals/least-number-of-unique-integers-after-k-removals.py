class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        freq = sorted(freq.values())
        remaining = len(freq)
        for f in freq:
            if k >= f:
                k -= f
                remaining -= 1
            else:
                break
        return remaining