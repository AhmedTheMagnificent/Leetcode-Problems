class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        def isWavy(i):
            x = str(i)
            if len(x) < 3:  return 0
            wavi = 0
            for i in range(1, len(x) - 1):
                if int(x[i - 1]) < int(x[i]) and int(x[i + 1]) < int(x[i]): wavi += 1
                elif int(x[i - 1]) > int(x[i]) and int(x[i + 1]) > int(x[i]): wavi += 1
            return wavi
        for i in range(num1, num2 + 1):
            waviness += isWavy(i)
        return waviness