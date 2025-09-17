class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        power = 0
        number = n
        while n > 0:
            power += 1
            n //= 2
        
        return 2 ** power - number - 1

        