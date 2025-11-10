class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2 = dict()
        for i, num in enumerate(nums2):
            num2[num] = i
        output = []
        for num in nums1:
            idx = num2[num]
            found = -1
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    found = nums2[j]
                    break
            output.append(found)
        return output