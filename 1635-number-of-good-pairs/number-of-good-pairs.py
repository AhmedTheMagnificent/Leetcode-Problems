class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1

        count = 0
        for value in hashMap.values():
            count += (value * (value - 1)) // 2

        return count