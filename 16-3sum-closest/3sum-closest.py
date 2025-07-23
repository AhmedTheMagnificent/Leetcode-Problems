class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                difference = abs(target - sum)
                if difference < abs(target - closest):
                    closest = sum
                if sum == target:
                    return closest
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return closest