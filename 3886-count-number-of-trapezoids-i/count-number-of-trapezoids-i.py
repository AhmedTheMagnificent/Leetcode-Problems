class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d = defaultdict(int)
        MOD = 10**9 + 7
        for x, y in points:
            d[y] += 1
        levels = list(d.values())
        count = 0
        comb = [lvl * (lvl - 1) // 2 for lvl in levels]
        total = 0
        cumSum = 0  # cumulative sum of C(n,2) seen so far
        
        for c in comb:
            total += cumSum * c
            total %= MOD
            cumSum += c
            cumSum %= MOD
        
        return total