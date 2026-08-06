class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(n):
            prod = 1
            for num in str(n):
                prod *= int(num)
            return prod
        while True:
            if product(n) % t == 0:  return n
            n += 1