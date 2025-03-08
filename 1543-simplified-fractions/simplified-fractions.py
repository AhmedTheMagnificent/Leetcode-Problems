class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        lis = []
        for i in range(1, n):
            for j in range(1, n + 1):
                if self.gcd(i, j) == 1 and (i != j) and j > i:
                    lis.append(f"{i}/{j}")
        return lis

    def gcd(self, a, b):
        while a > 0 and b > 0:
            if a >= b:
                a %= b
            else:
                b %= a
        return a + b
