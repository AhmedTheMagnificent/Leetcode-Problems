class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret = []
        for number in nums:
            if number > 9:
                num = number
                k = len(str(num)) - 1
                while k >= 0:
                    ret.append(num//(10 ** k))
                    num %= (10 ** k)
                    k -= 1
            else:
                ret.append(number)

        return ret