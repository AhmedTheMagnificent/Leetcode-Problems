class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = []
        maxi = max(candies)
        for i in candies:
            greatest.append(extraCandies+i >= maxi)
        return greatest