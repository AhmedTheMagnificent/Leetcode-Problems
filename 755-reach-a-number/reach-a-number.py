class Solution:
    def reachNumber(self, target: int) -> int:
        total = 0
        steps = 0
        target = abs(target)
        while total < target or (target - total) % 2 != 0:
            steps += 1
            total += steps
        return steps