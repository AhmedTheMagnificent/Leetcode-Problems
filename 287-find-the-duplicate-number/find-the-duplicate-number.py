class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                return num