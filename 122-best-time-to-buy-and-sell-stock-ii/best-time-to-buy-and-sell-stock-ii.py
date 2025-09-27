class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] >= 0:
                res += (prices[r] - prices[l])
                l = r
            else:
                if prices[l] > prices[r]:
                    l = r
                else:
                    l += 1
        
        return res