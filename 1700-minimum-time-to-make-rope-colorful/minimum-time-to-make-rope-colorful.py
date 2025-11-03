class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        output = 0
        max_time = neededTime[0]
        for i in range(1, len(neededTime)):
            if colors[i] == colors[i - 1]:
                output += min(max_time, neededTime[i])
                max_time = max(max_time, neededTime[i])
            else:
                max_time = neededTime[i]
            
        return output
