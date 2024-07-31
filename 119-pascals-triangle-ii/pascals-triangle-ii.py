class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lis = []
        for i in range(rowIndex + 1):
            lis.append(int(self.factorial(rowIndex) / (self.factorial(i) * self.factorial(rowIndex - i))))
        return lis

    def factorial(self, n):
        if n in [0, 1]:
            return 1
        else:
            return n * factorial(n-1)