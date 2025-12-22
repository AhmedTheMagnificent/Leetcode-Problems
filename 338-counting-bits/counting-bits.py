class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        def dp(i):
            if i == 0:
                return 0
            if output[i] != 0:
                return output[i]

            output[i] = dp(i // 2) + (i % 2)
            return output[i]

        for i in range(n + 1):
            dp(i)

        return output
