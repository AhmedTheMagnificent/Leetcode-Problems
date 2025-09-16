class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        def lcm(x, y):
            return abs(x * y) // gcd(x, y)

        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1:
                g = gcd(stack[-1], stack[-2])
                if g > 1:
                    stack.append(lcm(stack.pop(), stack.pop()))
                else:
                    break
        return stack
