class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def containZero(num):
            while num:
                a = num % 10
                if a == 0:
                    return True
                num //= 10
            return False
        for i in range(1, n + 1):
            a, b = i, n - i
            if not containZero(a) and not containZero(b):
                return [a, b]
            