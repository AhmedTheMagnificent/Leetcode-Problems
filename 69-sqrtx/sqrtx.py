class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x
        
        low, high = 0, x // 2
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
