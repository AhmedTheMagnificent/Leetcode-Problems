class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            n = 0
            found = False
            while n < num:
                if (n | (n + 1)) == num:   
                    found = True
                    break
                n += 1
            ans.append(n if found else -1)
        return ans