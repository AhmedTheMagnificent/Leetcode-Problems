class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                del m[num]
        return list(key for key in m.keys())