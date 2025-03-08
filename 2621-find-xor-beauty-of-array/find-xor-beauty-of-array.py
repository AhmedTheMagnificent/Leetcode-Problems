class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        number = 0
        for num in nums:
            number ^= num

        return number
