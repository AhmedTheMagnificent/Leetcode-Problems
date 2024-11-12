class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        permutations = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            current = nums[i]
            for p in self.permute(rest):
                permutations.append([current] + p)
        return permutations
