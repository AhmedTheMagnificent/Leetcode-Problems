class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min, max = float("inf"), -float("inf")
        for i in nums:
            if i < min:
                min = i
            if i > max:
                max = i
        return self.euclid(min, max)

    def euclid(self, x, y):
        while x > 0 and y > 0:
            if x >= y:
                x %= y
            else:
                y %= x
        return x + y