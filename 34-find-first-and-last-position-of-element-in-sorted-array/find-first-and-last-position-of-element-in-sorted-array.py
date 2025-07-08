class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, left, right, target, first):
            index = -1
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] == target:
                    index = mid
                    if first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        
        return [
            binarySearch(nums, 0, len(nums) - 1, target, True),
            binarySearch(nums, 0, len(nums) - 1, target, False)
        ]