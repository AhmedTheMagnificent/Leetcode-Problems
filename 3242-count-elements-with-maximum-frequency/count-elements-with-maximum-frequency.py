class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1
        max_freq = -float("inf")
        for num, freq in freqs.items():
            if freq > max_freq:
                max_freq = freq
        count = 0
        for num, freq in freqs.items():
            if freq == max_freq:
                count += freq
        return count