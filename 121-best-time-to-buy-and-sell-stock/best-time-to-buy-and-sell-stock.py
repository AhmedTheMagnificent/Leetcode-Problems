class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if (prices[i] - buy) > 0 and (prices[i] - buy) > max_profit:
                max_profit = prices[i] - buy
            elif prices[i] < buy:
                buy = prices[i]
        
        return max_profit