class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = n * (n + 1) // 2
        k = n // m
        num2 = m * k * (k + 1) // 2

        return num1 - 2 * num2
