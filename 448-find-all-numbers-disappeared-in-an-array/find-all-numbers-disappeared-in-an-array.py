class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        nums.sort()
        nums = set(nums)
        output = []
        for i in range(1, n):
            if i in nums:
                continue
            else:
                output.append(i)
        return output