class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        freq = {}
        count = 0
        for i in range(n):
            for j in range(n):
                if nums1[i] + nums2[j] not in freq:
                    freq[nums1[i] + nums2[j]] = 0
                freq[nums1[i] + nums2[j]] += 1
        
        for i in range(n):
            for j in range(n):
                if -(nums3[i] + nums4[j]) in freq:
                    count  += freq[-(nums3[i] + nums4[j])]
        return count