class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = 0
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[m + n - k - 1] = nums2[j]
                j -= 1
            else:
                nums1[m + n - k - 1] = nums1[i]
                i -= 1
            k += 1
        
        # Copy remaining elements from nums2 if any
        while j >= 0:
            nums1[m + n - k - 1] = nums2[j]
            j -= 1
            k += 1

        # No need to do anything for remaining elements in nums1
