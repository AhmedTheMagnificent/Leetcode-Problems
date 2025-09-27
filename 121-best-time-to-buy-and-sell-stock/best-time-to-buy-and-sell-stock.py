class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        res = 0

        for r in range(1, len(prices)):
            if prices[r] - prices[l] >= 0:
                res = max(res, prices[r] - prices[l])
            else:
                if prices[l] > prices[r]:
                    l = r
                else:
                    l += 1

        return res

        