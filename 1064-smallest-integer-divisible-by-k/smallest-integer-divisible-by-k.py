class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k & 1 == 0 or k % 5 == 0:
            return -1
        length = 0
        rem = 0
        while True:
            rem = (rem * 10 + 1) % k
            length += 1
            if rem == 0:
                return length