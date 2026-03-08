class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ret = ""
        for i in range(len(nums)):
            if nums[i][i] == '0':
                ret += "1"
            else:
                ret += "0"
        return ret