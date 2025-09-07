class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        even = 1 if n % 2 == 0 else 0
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        if not even:
            result.append(0)
        return result