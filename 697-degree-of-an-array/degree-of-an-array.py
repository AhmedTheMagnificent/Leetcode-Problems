class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = [1, i, i]
            else:
                hashMap[nums[i]][0] += 1
                hashMap[nums[i]][2] = i
        maximum = max(val[0] for val in hashMap.values())
        length = len(nums)
        for count, left, right in hashMap.values():
            if count == maximum:
                length = min(length, right - left + 1)
        return length