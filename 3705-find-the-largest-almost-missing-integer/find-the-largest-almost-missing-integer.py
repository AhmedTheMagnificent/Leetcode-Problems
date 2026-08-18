class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        ret = -1
        hashmap = {}
        for i in range(len(nums) - k + 1):
            s = set(nums[i: i + k])
            for num in s:
                if num not in hashmap:  hashmap[num] = 0
                hashmap[num] += 1
            candidates = list(key for key, value in hashmap.items() if value == 1)
        return max(candidates) if candidates else -1