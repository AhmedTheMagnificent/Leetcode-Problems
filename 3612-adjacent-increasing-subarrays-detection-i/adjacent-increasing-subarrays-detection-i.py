class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def isIncreasing(subarr):
            return all(subarr[i] < subarr[i + 1] for i in range(len(subarr) - 1))

        for i in range(n - 2 * k + 1):
            first = nums[i:i+k]
            second = nums[i+k:i+2*k]
            if isIncreasing(first) and isIncreasing(second):
                return True
        return False


