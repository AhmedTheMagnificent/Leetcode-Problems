class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        output = []
        for k, v in n1.items():
            if k in n2:
                value = min(v, n2[k])
                output.extend([k] * value)
        return output