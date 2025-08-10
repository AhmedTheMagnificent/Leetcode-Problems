class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        invm = {}
        for key, value in m.items():
            invm[value] = key

        return invm[1]