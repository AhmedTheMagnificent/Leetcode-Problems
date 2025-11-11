class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        freq = Counter(candyType)
        n = len(candyType) // 2
        return min(len(freq), n)