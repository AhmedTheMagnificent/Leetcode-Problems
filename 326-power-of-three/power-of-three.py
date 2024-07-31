class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n >= 3:
            while n >= 3:
                if n == 3:
                    return True
                else:
                    n = n/3
        elif n < 3:
            while n <= 3:
                if n == 3:
                    return True
                else:
                    n = n*3
        return False

        