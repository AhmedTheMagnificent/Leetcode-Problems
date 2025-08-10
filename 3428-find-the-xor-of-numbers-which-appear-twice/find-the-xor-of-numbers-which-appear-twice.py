class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        xor = 0
        for key, value in dic.items():
            if value == 2:
                xor ^= key
        return xor