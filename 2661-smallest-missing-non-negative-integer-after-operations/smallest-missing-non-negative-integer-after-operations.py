class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        for i in range(len(nums)):
            nums[i] %= value
        freq = [0] * value
        for i in range(len(nums)):
            freq[nums[i]] += 1

        min_freq = freq[0]
        min_idx = 0
        for i in range(1, value):
            if freq[i] < min_freq:
                min_freq = freq[i] 
                min_idx = i
        return min_idx + min_freq * value
