class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = {}
        output = []
        for num in nums:
            if num not in duplicates:
                duplicates[num] = 0
            duplicates[num] += 1
        for key, value in duplicates.items():
            if value == 2:
                output.append(key)
        return output