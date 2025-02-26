class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        eliminated = 0
        time = [d / s for d, s in zip(dist, speed)]
        time.sort()
        for i in time:
            if eliminated < i:
                eliminated += 1
            else:
                break
        return eliminated
