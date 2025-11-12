class Solution:
    def isHappy(self, n: int) -> bool:
        summ = n
        seen = set()
        while True:
            local = 0
            temp = summ
            while temp:
                remainder = temp % 10
                local += remainder ** 2
                temp //= 10
            summ = local
            if summ == 1:
                return True
            if summ in seen:
                return False
            seen.add(summ)