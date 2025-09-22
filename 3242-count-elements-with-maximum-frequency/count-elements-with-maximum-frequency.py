class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1
        max_freq = max(freqs.values())
        count = sum(freq for freq in freqs.values() if freq == max_freq)
        return count