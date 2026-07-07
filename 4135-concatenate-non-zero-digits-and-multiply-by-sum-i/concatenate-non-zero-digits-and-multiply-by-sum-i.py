class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:  return 0
        s = 0
        num = ""
        for i in str(n):
            num += i if i != '0' else ''
            s += int(i)
        return int(num) * s